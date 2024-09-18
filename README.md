Real-Time WLAN Channel Utilization Monitor

Table of Contents
Overview
Features
Prerequisites
Hardware Requirements
Software Requirements
Installation
1. Clone the Repository
2. Set Up Python Virtual Environment (Optional but Recommended)
3. Install Python Dependencies
4. Install System Dependencies
Configuration
1. Enable Monitor Mode on Wireless Interface
2. Verify TShark Installation
Usage
Command-Line Arguments
Running the Script
Examples
Understanding the Output
Troubleshooting
Contributing
License
Acknowledgements
Overview
The Real-Time WLAN Channel Utilization Monitor is a Python-based tool designed to monitor and visualize wireless LAN (WLAN) channel utilization in real-time. By capturing live network packets, processing them, and displaying utilization metrics, this tool aids network administrators and enthusiasts in assessing channel performance and identifying potential issues.

Features
Live Packet Capture: Utilizes pyshark to capture live packets from a specified wireless interface in monitor mode.
Real-Time Processing: Processes captured packets to calculate channel utilization over configurable time intervals.
Dynamic Visualization: Displays channel utilization percentages on an animated matplotlib plot, updating in real-time.
User-Friendly Interface: Accepts command-line arguments for easy configuration of interface, interval duration, and display settings.
Alerts on Inactivity: Notifies users if no packets are received for a specified duration, indicating potential issues with the sniffer setup.
Prerequisites
Hardware Requirements
Wireless Network Interface Card (NIC): A compatible wireless NIC that supports monitor mode. Ensure your NIC can capture the necessary wireless frames.
Supported Operating System: Primarily tested on Linux and macOS. Some functionalities might be limited or require additional configuration on Windows.
Software Requirements
Python: Version 3.6 or later.
TShark: Command-line version of Wireshark for packet capturing.
Installation
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/wlan-channel-utilization-monitor.git
cd wlan-channel-utilization-monitor
Replace yourusername and the repository URL with your actual GitHub username and repository link if applicable.

2. Set Up Python Virtual Environment (Optional but Recommended)
Using a virtual environment ensures that project dependencies are isolated from other Python projects.

bash
Copy code
python3 -m venv venv
Activate the virtual environment:

macOS/Linux:

bash
Copy code
source venv/bin/activate
Windows:

bash
Copy code
venv\Scripts\activate
3. Install Python Dependencies
With the virtual environment activated, install the required Python modules:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt, you can install the necessary packages directly:

bash
Copy code
pip install pyshark matplotlib
4. Install System Dependencies
a. Install TShark (Wireshark)
pyshark relies on TShark for packet capturing. Ensure TShark is installed on your system.

Ubuntu/Debian:

bash
Copy code
sudo apt-get update
sudo apt-get install tshark
During installation, you might be prompted to allow non-superusers to capture packets. Select "Yes" to proceed.

macOS (Using Homebrew):

bash
Copy code
brew install wireshark
During installation, you may be prompted to allow non-superusers to capture packets. Follow the on-screen instructions.

Windows:

Download Wireshark:
Visit the official Wireshark download page and download the installer for Windows.

Install Wireshark:
Run the installer and ensure that the TShark component is selected. Follow the on-screen instructions.

Add TShark to PATH:
During installation, opt to add TShark to your system's PATH. If not done automatically, manually add the TShark installation directory (e.g., C:\Program Files\Wireshark) to your PATH environment variable.

b. Verify TShark Installation
After installation, verify that TShark is correctly installed and accessible:

bash
Copy code
tshark --version
You should see version information displayed. If not, ensure that TShark is installed and added to your system's PATH.

Configuration
1. Enable Monitor Mode on Wireless Interface
Before running the script, ensure your wireless interface is set to monitor mode. The method to enable monitor mode varies based on the operating system and specific wireless hardware.

Linux:
Use airmon-ng to enable monitor mode.

Install aircrack-ng:

bash
Copy code
sudo apt-get install aircrack-ng
Enable Monitor Mode:

bash
Copy code
sudo airmon-ng start wlan0
Replace wlan0 with your actual wireless interface name.

Verify Mode:

bash
Copy code
iwconfig
Ensure that the interface is in monitor mode.

macOS:
List Interfaces:

bash
Copy code
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s
Enable Monitor Mode:

macOS requires different tools or commands to enable monitor mode. One common method is using airport utility:

bash
Copy code
sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport en0 sniff 6
Replace en0 with your actual wireless interface and 6 with the desired channel.

Windows:
Enabling monitor mode on Windows is more complex and may not be supported on all hardware. Ensure your wireless card supports monitor mode and consider using specialized drivers or tools.

2. Verify TShark Installation
Ensure that TShark is accessible and functioning correctly:

bash
Copy code
tshark --version
If TShark is not found, revisit the installation steps to ensure it's properly installed and added to your system's PATH.

Usage
Command-Line Arguments
The script accepts several command-line arguments to customize its behavior:

-i, --interface (Required):
Description: Wireless interface in monitor mode.
Example: wlan0mon, wlxf0a731becd1d
Usage: -i wlan0mon or --interface wlxf0a731becd1d

-d, --duration (Optional):
Description: Interval duration in seconds for calculating utilization.
Default: 5 seconds
Usage: -d 10 or --duration 10

-m, --max_points (Optional):
Description: Maximum number of data points to display on the plot.
Default: 0 (unlimited)
Usage: -m 100 or --max_points 100

-h, --help:
Description: Show help message and exit.

Running the Script
Activate Virtual Environment (If Used):

bash
Copy code
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Execute the Script:

bash
Copy code
python wlan_utilization_monitor.py -i <interface> -d <duration> -m <max_points>
Replace <interface>, <duration>, and <max_points> with your desired values.

Examples
Basic Usage with Default Settings:

Monitor wlan0mon interface with a 5-second interval and unlimited data points.

bash
Copy code
python wlan_utilization_monitor.py -i wlan0mon
Custom Interval Duration:

Monitor wlan0mon with a 10-second interval.

bash
Copy code
python wlan_utilization_monitor.py -i wlan0mon -d 10
Limited Data Points on Plot:

Display only the last 100 data points on the plot.

bash
Copy code
python wlan_utilization_monitor.py -i wlan0mon -m 100
Full Customization:

bash
Copy code
python wlan_utilization_monitor.py -i wlxf0a731becd1d -d 15 -m 200
Understanding the Output
Upon running the script, an animated matplotlib plot will appear displaying the real-time channel utilization. Additionally, an information box on the plot provides the following details:

Channel: Current channel number being monitored.
Packets Processed: Total number of packets processed since the start of the script.
Current Utilization: Latest channel utilization percentage.
Current Time: Timestamp of the latest update.
Plot Features:

X-Axis: Time in seconds since the script started.
Y-Axis: Channel Utilization Percentage (0% - 100%).
Dynamic Updates: The plot updates every second, reflecting the latest utilization data.
Alert Mechanism:

If no packets are received for 10 seconds, the script will print a warning message:

yaml
Copy code
No packets received for 10 seconds. The sniffer device might not be in monitor mode correctly.
The script will then terminate gracefully.

Troubleshooting
Common Issues and Solutions
TShark Not Found or pyshark Errors:

Symptom:
Errors related to TShark not being found or pyshark failing to initialize.

Solution:
Ensure TShark is installed and added to your system's PATH. Verify by running tshark --version. If TShark is installed in a non-standard location, specify its path in the script:

python
Copy code
capture = pyshark.LiveCapture(interface=self.interface, tshark_path='/path/to/tshark')
Permission Denied Errors:

Symptom:
Errors indicating insufficient permissions to capture packets.

Solution:

Linux/macOS:
Add your user to the wireshark group:

bash
Copy code
sudo usermod -aG wireshark $(whoami)
Then, log out and log back in for changes to take effect.

Windows:
Run the terminal or IDE with administrative privileges.

No Packets Captured:

Symptom:
The script runs but no data is displayed or utilization remains at 0%.

Solution:

Ensure the wireless interface is in monitor mode.
Verify that there is active wireless traffic.
Check for hardware compatibility and driver support.
Ensure TShark has the necessary permissions to capture packets.
Missing Packet Attributes (e.g., wlan_radio.duration):

Symptom:
Errors or zero values when accessing certain packet attributes.

Solution:

Not all wireless interfaces or drivers provide complete metadata. Consider updating drivers or using a different interface.
Modify the script to handle missing attributes gracefully.
High Memory Usage Over Time:

Symptom:
The script consumes increasing amounts of memory during prolonged use.

Solution:

Limit the number of data points using the --max_points argument.
Implement data persistence (e.g., logging to a file) and periodically clear in-memory data structures.
Contributing
Contributions are welcome! If you encounter issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

Steps to Contribute:

Fork the Repository

Create a Feature Branch

bash
Copy code
git checkout -b feature/YourFeature
Commit Your Changes

bash
Copy code
git commit -m "Add your message here"
Push to the Branch

bash
Copy code
git push origin feature/YourFeature
Open a Pull Request

License
This project is licensed under the MIT License.

Acknowledgements
PyShark: Python wrapper for TShark.
Matplotlib: Comprehensive library for creating static, animated, and interactive visualizations in Python.
Wireshark: Network protocol analyzer used for capturing and analyzing packets.
Contact
For any questions or support, please contact your.email@example.com.

Happy Monitoring! 🚀
