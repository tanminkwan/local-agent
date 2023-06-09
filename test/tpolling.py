import requests
import threading
from time import sleep
from polling2 import *
from tappender import Appender, appender

class Polling:

    def __init__(self, url: str, appender: Appender) -> None:
        self.startPolling(url)
        self.appender = appender

    def _get_response(self, response):
        return response.status_code == 200

    def _polling(self, url):

        while True:
            try:
                result = poll(lambda: requests.get(url), 
                                step=10, 
                                poll_forever=True,
                                check_success=self._get_response)
            except requests.exceptions.ConnectionError as e:
                self.appender.printUrJob('result ConnectionError')
                sleep(30)
                continue

            self.appender.printUrJob('result : ' + result.text)

    def startPolling(self, url):

        thread = threading.Thread(target=self._polling, args=(url,))
        thread.name = '_polling'
        thread.start()

if __name__ == '__main__':
    Polling('http://localhost:8809', appender)