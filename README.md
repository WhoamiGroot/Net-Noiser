Simple Network Noiser in python3. in plain and Tor function.
install:
```
pip install requests
```
```
python3 netnoiser.py
```
Make sure your combo list is named websites.txt and run the script.

in TOR:

Instructions to Run:

    Start Tor:
        If Tor isn't already running, open your terminal and start the Tor service with:
```
tor
```
    This should make Tor available at 127.0.0.1:9050 (the default address).

Install Required Libraries:
```
pip install requests requests[socks]
```
I used the 10million weblist. You can download others if you want to from the list below:

Credits to: https://github.com/PeterDaveHello/top-1m-domains
for the domainlists.

The script is swtiching every 1 to 4 seconds (You can change this in the script) from page and sometimes it throws some errors but this is normal. Don't worry not every websites works anymore, and i am not planning to filter 10 million websites.

Normal use:
![normal](https://github.com/user-attachments/assets/b432ef30-c47c-4e4d-aac3-cff4137925b3)

over Tor:
![tor](https://github.com/user-attachments/assets/5d281b20-fea8-444e-974b-822dc765e82a)

If you want to sort out valid URLs and non malicious URLS,

Here's how you can approach it:
Step-by-Step Guide:

Check for Valid URLs:

You can use a Python script to validate URLs. Use the requests library to check if a URL is valid or reachable.

Here's a sample Python script for validating URLs:
```
import requests
from urllib.parse import urlparse

def add_scheme(url):
    """Add 'https://' to the URL if no scheme is provided."""
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'https://' + url  # Default to https://
    return url

def is_valid_url(url):
    """Check if the URL is valid and accessible."""
    url = add_scheme(url)  # Ensure the URL has a scheme
    try:
        response = requests.get(url, timeout=5)  # Adjust the timeout value if needed
        if response.status_code == 200:
            return True
        else:
            print(f"Invalid URL (status {response.status_code}): {url}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error with URL {url}: {e}")
        return False

def validate_urls(input_file, output_file):
    """Read URLs from a file, check if valid, and save valid ones."""
    valid_urls = []

    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            if url:  # Make sure it's not an empty line
                if is_valid_url(url):
                    valid_urls.append(url)
                else:
                    print(f"Skipping invalid URL: {url}")

    with open(output_file, 'w') as out_file:
        for url in valid_urls:
            out_file.write(url + '\n')
    print(f"Valid URLs saved to {output_file}")

if __name__ == "__main__":
    input_file = 'website.txt'  # Change to your file name
    output_file = 'valid_urls.txt'  # This is where the valid URLs will be saved
    validate_urls(input_file, output_file)

```

This will check each URL in website.txt, and only valid (reachable) URLs will be written to valid_urls.txt.

Check for Malicious URLs:

For detecting malicious URLs, you can integrate an external service or API that checks URL safety, like:
     Google Safe Browsing API
     VirusTotal API

For instance, using the Google Safe Browsing API with Python:
```
        import requests
        import json

        def check_malicious(url):
            api_key = 'YOUR_GOOGLE_SAFE_BROWSING_API_KEY'
            endpoint = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'

            body = {
                "client": {
                    "clientId": "yourClientId",
                    "clientVersion": "1.5.2"
                },
                "threatInfo": {
                    "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                    "platformTypes": ["ANY_PLATFORM"],
                    "threatEntryTypes": ["URL"],
                    "threatEntries": [{"url": url}]
                }
            }

            response = requests.post(endpoint, json=body)
            result = response.json()

            return "matches" in result

        with open('valid_urls.txt', 'r') as file:
            safe_urls = []
            for line in file:
                url = line.strip()
                if not check_malicious(url):  # If URL is not malicious
                    safe_urls.append(url)

        with open('safe_urls.txt', 'w') as out_file:
            for url in safe_urls:
                out_file.write(url + '\n')
```
This will check each valid URL against Google's Safe Browsing service and remove any malicious ones.

Combine the two steps:
        First, use the script to validate URLs.
        Then, use the second script to remove malicious URLs from the list.

Tools and Libraries Needed:

Python
requests library (pip install requests)
Google Safe Browsing or VirusTotal API keys (both are free for limited usage, but you might need a paid plan for large volumes)

If you'd like more help with specific parts of the code or setup, let me know!
