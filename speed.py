import speedtest

def calculate_bandwidth(speed):
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
