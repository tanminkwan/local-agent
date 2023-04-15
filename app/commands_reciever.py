import json
import requests
import threading
from time import sleep
from polling2 import *
from .executer import Executer
        
class CommandsReciever:

    def __init__(self, url: str, executer: Executer) -> None:
        self.executer = executer
        self.start_polling(url)

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
                sleep(30)
                continue

            print('result : ',type(result.text), result.text)
            result_dict = json.loads(result.text)
            rtn, message = self.executer.executeCommands(result_dict)

    def start_polling(self, url):

        thread = threading.Thread(target=self._polling, args=(url,))
        thread.name = '_polling'
        thread.start()