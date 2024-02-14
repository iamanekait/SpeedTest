# Internet Speed Tester

This Python script allows you to test your internet connection speed using the Speedtest.net service.

## Installation

You need to install the `speedtest-cli` library:

```bash
pip install speedtest-cli
```

## Usage

```python
import speedtest

def calculate_bandwidth(speed):
    """
    Calculate bandwidth category based on speed.

    Parameters:
    - speed (float): The speed in MB/s.

    Returns:
    - str: The bandwidth category.
    """
    if speed < 1:
        return "Very Slow"
    elif 1 <= speed < 10:
        return "Slow"
    elif 10 <= speed < 50:
        return "Moderate"
    elif 50 <= speed < 100:
        return "Fast"
    else:
        return "Very Fast"

def check_internet_speed():
    """
    Test internet speed and print results.
    """
    st = speedtest.Speedtest()
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download() / 8_000_000  # Convert to MB/s
    download_bandwidth = calculate_bandwidth(download_speed)
    print(f"Download Speed: {download_speed:.2f} MB/s ({download_bandwidth})")

    print("Testing upload speed...")
    upload_speed = st.upload() / 8_000_000  # Convert to MB/s
    upload_bandwidth = calculate_bandwidth(upload_speed)
    print(f"Upload Speed: {upload_speed:.2f} MB/s ({upload_bandwidth})")

    print("Testing ping time to 8.8.8.8...")
    ping_time = st.results.ping
    print(f"Ping Time to 8.8.8.8: {ping_time:.2f} ms")

if __name__ == "__main__":
    check_internet_speed()
```

### Explanation

- The script measures download and upload speeds, as well as ping time to a predefined server (`8.8.8.8`).
- It categorizes the speed into different bandwidth levels (`Very Slow`, `Slow`, `Moderate`, `Fast`, `Very Fast`) based on predefined thresholds.
- The `speedtest-cli` library is used to perform the speed tests.

## Notes

- Make sure to have a stable internet connection before running the script.
- The accuracy of the speed test results may vary depending on various factors such as network congestion and server load.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
