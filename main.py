from concurrent.futures import ThreadPoolExecutor
import requests
from time import sleep
from data_gen import new_payload

# test URL
# URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdas_WPB6OzwCGh2pOyaFYkovAUJeE9-7KapjLqTq0xbpkwVA/formResponse?pli=1"

# test payload
# payload = {
#     "entry.131900708": "testt",
#     "entry.1804986014": "ans1",
#     "entry.1010018223": "Option 1",
#     "entry.1010018223": "Option 2",
#     "entry.1010018223": "Option 3",
# }

URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSefeUcLXD-gKFTxeuzJsbirEnQT-TrIvAcRyGYjnlDC23jLBQ/formResponse?pli=1"

payload = new_payload()


def main():
    for _ in range(1):
        #sleep(5)
        r = requests.post(URL, data=payload)

        if r.ok:
            print("Submitted successfully!", r.status_code)
        else:
            print("Failed:", r.status_code)

def work():
    num_threads = 1

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            executor.submit(main)

if __name__ == "__main__":
    work()
