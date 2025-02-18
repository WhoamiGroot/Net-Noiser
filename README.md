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
![1](https://github.com/user-attachments/assets/96c60bc1-b4fb-4d86-b198-b28f75d6b08e)

