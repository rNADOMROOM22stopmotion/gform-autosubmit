import requests
from time import sleep
URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdas_WPB6OzwCGh2pOyaFYkovAUJeE9-7KapjLqTq0xbpkwVA/formResponse"

payload = {
    "entry.131900708": "hellllo",
    "entry.1804986014": "ans2",
    "entry.1010018223": ["Option 2", "Option 3"],
    "emailAddress": "xxxx@gmail.com"
}
headers = {
    "User-Agent": "xxxxx",
    "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSdas_WPB6OzwCGh2pOyaFYkovAUJeE9-7KapjLqTq0xbpkwVA/viewform?fbzx=-3081672792433221379"
}
cookies = {
    "SID": "xxxxx",
    "HSID": "xxxxx",
    "SSID": "xxxxx"
}

def main():
    for _ in range(40):
        sleep(0.2)
        r = requests.post(URL, data=payload, headers=headers, cookies=cookies)
        if r.ok:
            print("Submitted successfully!", r.status_code)
        else:
            print("Failed:", r.status_code)


if __name__ == "__main__":
    main()