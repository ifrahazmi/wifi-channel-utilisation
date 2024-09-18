import pyshark
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import queue
import time
from datetime import datetime
import argparse

__author__ = "Ifrahuddin Azmi"
__doc__ = "Support Python3 and Above"
__version__ = "v1.0"

class PacketCapturer(threading.Thread):
    def __init__(self, interface, packet_queue, stop_event):
        threading.Thread.__init__(self)
        self.interface = interface
        self.packet_queue = packet_queue
        self.stop_event = stop_event

    def run(self):
        # Live capture on the specified interface
        capture = pyshark.LiveCapture(interface=self.interface)
        try:
            # Start capturing packets
            for packet in capture.sniff_continuously():
                if self.stop_event.is_set():
                    break
                self.packet_queue.put(packet)
        except Exception as e:
            print(f"Error in PacketCapturer: {e}")
        finally:
            capture.close()

class PacketProcessor(threading.Thread):
    def __init__(self, packet_queue, interval_duration, utilization_queue, channel_queue, stop_event, no_packet_event):
        threading.Thread.__init__(self)
        self.packet_queue = packet_queue
        self.interval_duration = interval_duration
        self.utilization_queue = utilization_queue
        self.channel_queue = channel_queue
        self.stop_event = stop_event
        self.no_packet_event = no_packet_event
        self.interval_start_time = None
        self.interval_wlan_duration = 0.0
        self.channel_number = None
        self.total_packets_processed = 0
        self.last_packet_time = time.time()

    def run(self):
        while not self.stop_event.is_set():
            try:
                # Get the packet from the queue
                packet = self.packet_queue.get(timeout=1)
                self.total_packets_processed += 1
                packet_time = float(packet.sniff_timestamp)
                self.last_packet_time = time.time()

                # Access the wlan_radio.duration field
                if hasattr(packet, 'wlan_radio') and hasattr(packet.wlan_radio, 'duration'):
                    wlan_duration = int(packet.wlan_radio.duration) / 1e6  # Convert to seconds
                else:
                    wlan_duration = 0.0  # If not available, set to zero

                # Extract the channel frequency
                if hasattr(packet, 'radiotap') and hasattr(packet.radiotap, 'channel_freq'):
                    channel_freq = int(packet.radiotap.channel_freq)
                    # Map frequency to channel number
                    self.channel_number = self.freq_to_channel(channel_freq)
                    # Put the channel number into the channel_queue
                    self.channel_queue.put(self.channel_number)
                else:
                    # If channel frequency is not available, set to None
                    self.channel_number = None

                # Optional: Print durations and channel for debugging
                print(f"Packet Time: {packet_time:.6f}, WLAN Duration: {wlan_duration*1e6:.2f} μs, Channel: {self.channel_number}")

                if self.interval_start_time is None:
                    self.interval_start_time = packet_time

                # Check if the current packet is within the current interval
                if packet_time - self.interval_start_time <= self.interval_duration:
                    self.interval_wlan_duration += wlan_duration
                else:
                    # Calculate utilization for the interval
                    wlan_utilization = (self.interval_wlan_duration / self.interval_duration) * 100

                    self.utilization_queue.put((self.interval_start_time, wlan_utilization, self.total_packets_processed, self.channel_number))

                    # Reset for the next interval
                    while packet_time - self.interval_start_time > self.interval_duration:
                        self.interval_start_time += self.interval_duration
                    self.interval_wlan_duration = wlan_duration  # Start counting from the current packet

            except queue.Empty:
                # Check if no packet has been received for 10 seconds
                if time.time() - self.last_packet_time > 10:
                    print("No packets received for 10 seconds. The sniffer device might not be in monitor mode correctly.")
                    self.no_packet_event.set()
                    self.stop_event.set()
                continue
            except Exception as e:
                print(f"Error processing packet: {e}")
                continue

    def freq_to_channel(self, freq):
        # Map frequency to channel number for 2.4 GHz and 5 GHz bands
        freq_channel_map = {
            # 2.4 GHz band
            2412: 1,
            2417: 2,
            2422: 3,
            2427: 4,
            2432: 5,
            2437: 6,
            2442: 7,
            2447: 8,
            2452: 9,
            2457: 10,
            2462: 11,
            2467: 12,
            2472: 13,
            2484: 14,
            # 5 GHz band
            5180: 36,
            5200: 40,
            5220: 44,
            5240: 48,
            5260: 52,
            5280: 56,
            5300: 60,
            5320: 64,
            5500: 100,
            5520: 104,
            5540: 108,
            5560: 112,
            5580: 116,
            5600: 120,
            5620: 124,
            5640: 128,
            5660: 132,
            5680: 136,
            5700: 140,
            5745: 149,
            5765: 153,
            5785: 157,
            5805: 161,
            5825: 165,
        }
        return freq_channel_map.get(freq, None)

class PlotAnimator:
    def __init__(self, utilization_queue, start_time, info_dict, stop_event, max_points=None):
        self.utilization_queue = utilization_queue
        self.start_time = start_time
        self.info_dict = info_dict
        self.stop_event = stop_event
        self.x_data = []
        self.y_data = []
        self.fig, self.ax = plt.subplots()
        self.max_points = max_points  # Maximum number of data points to display

    def animate(self, i):
        while not self.utilization_queue.empty():
            interval_start_time, wlan_utilization, total_packets_processed, channel_number = self.utilization_queue.get()
            self.x_data.append(interval_start_time - self.start_time)
            self.y_data.append(wlan_utilization)
            # Update the info_dict
            self.info_dict['channel_number'] = channel_number
            self.info_dict['total_packets_processed'] = total_packets_processed
            self.info_dict['current_utilization'] = f"{wlan_utilization:.2f}%"
            self.info_dict['current_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if self.max_points and len(self.x_data) > self.max_points:
                self.x_data.pop(0)
                self.y_data.pop(0)
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, marker='o', label='Channel Utilization')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Channel Utilization (%)')
        self.ax.set_title('Real-Time Channel Utilization')

        # Add additional info as text on the plot
        info_text = (
            f"Channel: {self.info_dict.get('channel_number', 'N/A')}\n"
            f"Packets Processed: {self.info_dict.get('total_packets_processed', 0)}\n"
            f"Current Utilization: {self.info_dict.get('current_utilization', '0.00%')}\n"
            f"Current Time: {self.info_dict.get('current_time', '')}"
        )
        self.ax.text(
            0.95, 0.95, info_text, transform=self.ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        )

        self.ax.set_ylim(0, 100)
        self.ax.legend()
        self.ax.grid(True)

        # If stop_event is set, stop the animation
        if self.stop_event.is_set():
            plt.close(self.fig)

    def start(self):
        ani = animation.FuncAnimation(
            self.fig, self.animate, interval=1000, cache_frame_data=False
        )
        plt.show()

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Real-Time WLAN Channel Utilization Monitor')
    parser.add_argument('-i', '--interface', required=True, help='Wireless interface in monitor mode')
    parser.add_argument('-d', '--duration', type=int, default=5, help='Interval duration in seconds')
    parser.add_argument('-m', '--max_points', type=int, default=50, help='Maximum number of data points to display (0 for unlimited)')
    args = parser.parse_args()

    interface = args.interface
    interval_duration = args.duration
    max_points = args.max_points if args.max_points > 0 else None  # Set to None if 0

    # Queues for inter-thread communication
    packet_queue = queue.Queue()
    utilization_queue = queue.Queue()
    channel_queue = queue.Queue()
    stop_event = threading.Event()
    no_packet_event = threading.Event()

    # Start time
    start_time = time.time()

    # Start the packet capture thread
    packet_capturer = PacketCapturer(interface, packet_queue, stop_event)
    packet_capturer.start()

    # Start the packet processing thread
    packet_processor = PacketProcessor(packet_queue, interval_duration, utilization_queue, channel_queue, stop_event, no_packet_event)
    packet_processor.start()

    # Plotting setup
    info_dict = {}
    plot_animator = PlotAnimator(utilization_queue, start_time, info_dict, stop_event, max_points=max_points)

    try:
        plot_animator.start()
    except KeyboardInterrupt:
        print("Interrupted by user")
    finally:
        # Stop threads
        stop_event.set()
        packet_capturer.join()
        packet_processor.join()

    if no_packet_event.is_set():
        print("Program terminated due to no packets received for 10 seconds.")

    print("Program terminated.")

if __name__ == "__main__":
    main()
