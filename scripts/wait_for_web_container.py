from http.client import RemoteDisconnected
from time import sleep
from urllib import request
from urllib.error import URLError, HTTPError


def handler():
    retries = 20
    for retry in range(0, retries):
        try:
            status_code = request.urlopen('http://127.0.0.1:8000/').getcode()
        except (URLError, HTTPError, RemoteDisconnected):
            status_code = 500
        if status_code == 200:
            print('Web container is up.')
            exit(0)
        print(f'Web container not up. Try {retry + 1} of {retries}.')
        sleep(2)
    print(f'Web container failed to become available.')
    exit(1)


if __name__ == '__main__':
    handler()
