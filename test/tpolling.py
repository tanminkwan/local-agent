import requests
import threading
from time import sleep
from polling2 import *
from tappender import appender
        
def __get_response(response):
    return response.status_code == 200

def __polling(url):

    while True:
        try:
            result = poll(lambda: requests.get(url), 
                            step=10, 
                            poll_forever=True,
                            check_success=__get_response)
        except requests.exceptions.ConnectionError as e:
            appender.printUrJob('result ConnectionError')
            sleep(30)
            continue

        appender.printUrJob('result : ' + result.text)

def polling(url):

    thread = threading.Thread(target=__polling, args=(url,))
    thread.name = '__polling'
    thread.start()

if __name__ == '__main__':
    polling('http://localhost:8808')