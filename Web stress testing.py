import requests
import threading

# Number of requests to make
num_requests = 100

# URL to test
url = "https://example.com"

def make_request():
    """Make a single request to the specified URL"""
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed: {e}")

# Create and start threads
threads = []
for _ in range(num_requests):
    thread = threading.Thread(target=make_request)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All requests complete!")
