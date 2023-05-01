import json
import requests
import threading
from time import sleep
from polling2 import *
from .executer import ExecuterCaller
        
class CommandsReciever:

    def __init__(self, url: str, event: threading.Event) -> None:
        self.event = event
        self._start_polling(url)

    def get_thread(self):
        return self.thread
    
    def _get_response(self, response):
        return response.status_code == 200

    def _polling(self, url):

        while True:

            if self.event.is_set():
                print('[CommandsReciever is broken]')
                break

            try:
                result = poll(lambda: requests.get(url), 
                                step=10, 
                                poll_forever=True,
                                check_success=self._get_response)
            except requests.exceptions.ConnectionError as e:
                sleep(10)
                continue

            print('result : ',type(result.text), result.text)
            result_dict = json.loads(result.text)

            #self.lock.locked()
            rtn, message = ExecuterCaller.instance().execute_command(result_dict)
            #self.lock.release()

    def _start_polling(self, url):

        self.thread = threading.Thread(target=self._polling, args=(url,))
        self.thread.name = '_polling'
        self.thread.start()
        #self.thread.join()