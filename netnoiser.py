import requests
import random
import time
import re

def load_websites(filename="websites.txt"):
    """Loads the list of websites from the provided file and cleans them."""
    cleaned_websites = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                url = line.strip()  # Remove leading/trailing spaces
                if url:
                    # Remove any leading commas or other unwanted characters
                    url = re.sub(r'^[^a-zA-Z0-9]+', '', url)
                    
                    # Add 'https://' if no scheme is present
                    if not url.startswith(('http://', 'https://')):
                        url = 'https://' + url  # Default to https
                    
                    cleaned_websites.append(url)
        print(f"Loaded and cleaned {len(cleaned_websites)} websites.")
        return cleaned_websites
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        exit(1)

def fetch_random_website(websites):
    """Fetches a random website from the list and logs the status."""
    url = random.choice(websites)
    try:
        # Make a normal HTTP request
        response = requests.get(url, timeout=10)
        print(f"Fetched {url} with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

def network_noise(websites):
    """Simulates network noise by requesting random URLs from the list at random intervals."""
    while True:
        fetch_random_website(websites)
        sleep_time = random.randint(1, 4)  # Sleep for 1 to 4 seconds
        time.sleep(sleep_time)

if __name__ == "__main__":
    websites = load_websites("websites.txt")
    print("Starting network noise simulation...")
    network_noise(websites)

