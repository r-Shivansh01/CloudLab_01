import requests

def check_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Success! {url} is Online.")
        else:
            print(f"Alert! {url} returned {response.status_code}")
    except:
        print(f"Critical: Could not connect to {url}")

check_server("https://www.google.com")
print("Running from Disk D! update")
print("The Project is in progress....")
