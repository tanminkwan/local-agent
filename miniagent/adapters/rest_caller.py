from ..adapter import Adapter
from ..event_sender import get, post

class RESTCaller(Adapter):

    def call_get(self, url: str, params: dict = {}, headers: dict = {}) -> tuple[int, dict]:

        try:
            response = get(url, params=params, headers=headers, timeout=10)
            status = response.status_code
            if status == 204:
                result = {"message":"No content"}
            else:
                result = response.json()

        except ConnectionError as e:
            return -1, {"message":"ConnectionError to {}".format(url)}
        
        return status, result
    
    def call_post(self, url: str, json: dict, headers: dict = {}) -> tuple[int, dict]:

        try:
            response = post(url, json=json, headers=headers, timeout=10)
            status = response.status_code
            
            if status == 204:
                result = {"message":"No content"}
            else:
                result = response.json()
            
        except ConnectionError as e:
            return -1, {"message":"ConnectionError to {}".format(url)}
        
        return status, result

    def get_status(self) -> int:
        return 1