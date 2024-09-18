<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="20%" alt="WIFI-CHANNEL-UTILISATION-logo">
</p>
<p align="center">
    <h1 align="center">WIFI-CHANNEL-UTILISATION</h1>
</p>
<p align="center">
    <em><code>❯ Developer: Ifrahuddin Azmi</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/ifrahazmi/wifi-channel-utilisation?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/ifrahazmi/wifi-channel-utilisation?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/ifrahazmi/wifi-channel-utilisation?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/ifrahazmi/wifi-channel-utilisation?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python3">
</p>

<br>

#####  Table of Contents

- [ Overview](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#overview)
- [ Features](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#features)
- [ Repository Structure](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#repository-structure)
- [ Modules](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#modules)
- [ Getting Started](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#getting-started)
    - [ Prerequisites](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#prerequisites)
    - [ Installation](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#installation)
    - [ Usage](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#usage)
    - [ Extra Agrument](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#extra-agrument)
- [ Project Roadmap](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#project-roadmap)
- [ Contributing](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#contributing)
- [ License](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#license)
- [ Acknowledgments](https://github.com/ifrahazmi/wifi-channel-utilisation/tree/main?tab=readme-ov-file#acknowledgments)

---

##  Overview

<code>❯ The Real-Time WLAN Channel Utilization Monitor is a powerful Python-based tool designed to monitor and visualize wireless LAN channel utilization in real-time. As wireless networks become increasingly complex and congested, understanding channel usage is critical for maintaining optimal performance and ensuring a seamless user experience. This tool plays a vital role in capturing live network packets, providing insights into how channels are being utilized at any given moment.
</code>

<code>❯ By deploying this monitor, network administrators can gain a clear view of channel occupancy, identifying potential bottlenecks and areas of interference. The real-time data collection allows users to visualize network traffic patterns, making it easier to assess performance issues and optimize channel allocation. The graphical interface presents the information in an intuitive manner, enabling quick decisions based on current network conditions.
</code>

<code>❯ One of the key features of the Real-Time WLAN Channel Utilization Monitor is its ability to capture live packets, which are then analyzed to provide detailed statistics regarding channel utilization. This includes metrics such as the number of active devices, the types of traffic being transmitted, and the overall load on each channel. By analyzing this data, users can pinpoint specific times when congestion occurs, facilitating targeted interventions to improve network performance.
</code>

<code>❯ **In summary, the Real-Time WLAN Channel Utilization Monitor is an essential tool for anyone looking to manage WLAN performance effectively. With its capability to visualize real-time utilization and capture live packet data, it empowers users to make informed decisions that enhance the overall efficiency of their wireless networks.
</code>

---

##  Features

The Real-Time WLAN Channel Utilization Monitor is equipped with several key features that enhance its functionality and usability for network administrators and engineers. Below are the primary features that make this tool a must-have for monitoring wireless LAN performance:

#####  Live Packet Capture with Pyshark

Using the powerful Pyshark library, the monitor captures live packets from the WLAN. This feature allows users to analyze traffic in real-time, providing a snapshot of the network's current state. The captured packets include essential data such as source and destination addresses, protocols used, and traffic types, ensuring comprehensive insights into network activity.

#####  Real-Time Processing for Channel Utilization

The tool processes the captured packets in real-time, calculating channel utilization metrics on-the-fly. This dynamic processing enables users to observe how much bandwidth is being consumed at any given moment, facilitating prompt responses to network issues. By keeping track of channel occupancy, users can identify periods of congestion and adjust configurations as necessary.

#####  Dynamic Visualization with Matplotlib

Data visualization plays a crucial role in network monitoring. The Real-Time WLAN Channel Utilization Monitor leverages Matplotlib to create dynamic graphical representations of channel utilization. These visualizations update in real-time, allowing users to quickly interpret data trends and make informed decisions. The graphical interface is designed to be intuitive, making it easy for users to spot anomalies and inefficiencies.

#####  User-Friendly Command-Line Interface

The tool features a user-friendly command-line interface (CLI) that simplifies interaction with the monitor. Users can easily start and stop monitoring sessions, view real-time statistics, and access historical data through straightforward commands. This CLI design caters to both novice and experienced users, ensuring that everyone can utilize the monitor effectively.

#####  Alert Mechanisms for Inactivity

To enhance network management, the monitor includes alert mechanisms that notify users of inactivity or other critical events. These alerts can be configured to trigger notifications when channel utilization drops below a certain threshold or when no traffic is detected for an extended period. This feature helps ensure that network administrators can take immediate action to address potential issues before they escalate

---

##  Repository Structure

```sh
└── wifi-channel-utilisation/
    ├── LICENSE
    ├── Live_Channel_Utilization.py
    └── README.md
```

---

##  Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [Live_Channel_Utilization.py](https://github.com/ifrahazmi/wifi-channel-utilisation/blob/main/Live_Channel_Utilization.py) | <code>❯ Real-Time WLAN Channel Utilization Monitor</code> |

</details>

---

##  Getting Started

###  Prerequisites

**Python**: `version 3.10.12 or above`

###  Installation

Build the project from source:

1. Clone the wifi-channel-utilisation repository:
```sh
❯ git clone https://github.com/ifrahazmi/wifi-channel-utilisation
```

2. Navigate to the project directory:
```sh
❯ cd wifi-channel-utilisation
```

3. Install the required python dependencies:
```sh
❯ pip install pyshark matplotlib
```

4. Install the tshark dependencies:
```sh
❯ sudo apt-get update
❯ sudo apt-get install tshark
```

###  Usage

To run the project, execute the following command:

1. Enable Monitor Mode on Wireless Interface

Linux:
  Use airmon-ng to enable monitor mode.

1.1 Install aircrack-ng:
```sh
❯sudo apt-get install aircrack-ng
```

1.2 Enable Monitor Mode in Specific Channel:
```sh
❯sudo airmon-ng start <wireless interface> <channel_number>
```

1.3 Run The Script

```sh
❯ sudo python3 Live_Channel_Utilization.py -i <wireless interface>
```

###  Extra Agrument

Execute the following command as per need:

```sh
❯ sudo python3 Live_Channel_Utilization.py -i <wireless interface> -d <interval duration> -m <max points on garph>
```
 - -i --interface  Wireless interface in monitor mode
 - -d --duration   Interval duration in seconds
 - -m --max_points Maximum number of data points to display (0 for unlimited)

---

##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement basic features.</strike>
- [ ] **`Task 2`**: Implement for multiple channel.
- [ ] **`Task 3`**: Implement save pcap file parallel.

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/ifrahazmi/wifi-channel-utilisation/issues)**: Submit bugs found or log feature requests for the `wifi-channel-utilisation` project.
- **[Submit Pull Requests](https://github.com/ifrahazmi/wifi-channel-utilisation/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/ifrahazmi/wifi-channel-utilisation/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ifrahazmi/wifi-channel-utilisation
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/ifrahazmi/wifi-channel-utilisation/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=ifrahazmi/wifi-channel-utilisation">
   </a>
</p>
</details>

---

##  License

This project is protected under the [MIT LICENSE](https://opensource.org/license/mit) License. For more details, refer to the [LICENSE](https://github.com/ifrahazmi/wifi-channel-utilisation/blob/main/LICENSE) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
