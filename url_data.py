import requests
import threading


def site_data():
    site = input("Enter site:\n")
    r = requests.get(site)
    print(r.text)


threading.Thread(target=site_data, args=()).start()
