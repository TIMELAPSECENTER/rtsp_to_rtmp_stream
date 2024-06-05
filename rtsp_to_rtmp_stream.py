#!/usr/bin/env python3
import subprocess
import time
import platform
import os

# Set Variables
rtmp = 'rtmp://ip:port/key'
rtsp = 'rtsp://admin:admin@ip:port/Streaming/Channels/101'
reload_time_min = 30


def run_ffmpeg_linux():
    command = [
        'ffmpeg',
        '-i', rtsp,
        '-c', 'copy',
        '-f', 'flv',
        rtmp
    ]

    try:
        process = subprocess.Popen(command)
        reload_time_sec = reload_time_min * 60
        process.wait(timeout=reload_time_sec)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()


def run_ffmpeg_windows():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ffmpeg_path = os.path.join(dir_path, 'ffmpeg.exe')
    #ffmpeg_path = 'C:\\rtmp_stream\\ffmpeg.exe'

    command = [
        ffmpeg_path,
        '-i', rtsp,
        '-c', 'copy',
        '-f', 'flv',
        rtmp
    ]

    try:
        process = subprocess.Popen(command, shell=True)
        reload_time_sec = reload_time_min * 60
        process.wait(timeout=reload_time_sec)
    except subprocess.TimeoutExpired:
        process.terminate()
        process.communicate()


def main():
    os_type = platform.system()
    while True:
        print(f"Starting ffmpeg broadcasting on {os_type}...")
        if os_type == "Linux":
            run_ffmpeg_linux()
        elif os_type == "Windows":
            run_ffmpeg_windows()
        else:
            print("Unsupported operating system.")
            break  # Exit the loop if the OS is neither Linux nor Windows


if __name__ == "__main__":
    main()
