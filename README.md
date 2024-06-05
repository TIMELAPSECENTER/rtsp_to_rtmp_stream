# CCTV to Time-Lapse Center Streaming Tool

This program facilitates the streaming of CCTV camera feeds from a local network to the timelapse shooting service at [Timelapse Center](http://timelapse.center). It leverages `ffmpeg` to convert RTSP video streams to RTMP format and ensures robust connection maintenance, even in cases of network failures or interruptions.

The tool is designed to run on a local network computer connected to the CCTV, making it ideal for cameras without static IP addresses. Additionally, this solution supports video streaming to various social platforms such as YouTube, Facebook, Twitter, Twitch, Instagram, and LinkedIn.

## Features

- **RTSP to RTMP Conversion**: Converts RTSP streams from local CCTV cameras to RTMP format.
- **Dynamic IP Support**: Enables cameras without fixed IP addresses to connect to the Timelapse Center service.
- **OS Compatibility**: Automatically detects and adjusts to the Linux or Windows operating systems.

## Installation

Follow these steps to set up the streaming tool:

1. Clone the repository or download the program files:
   git clone https://github.com/TIMELAPSECENTER/rtsp_to_rtmp_stream.git
2. Navigate to the program directory:
   cd rtsp_to_rtmp_stream
3. Run the program:
   python rtsp_to_rtmp_stream.py
4. (Optional) Configure the program to automatically launch on system startup.
