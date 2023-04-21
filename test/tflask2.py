import sys
import json
import threading
from flask import Flask, request
from flask_api import status

global CNT, CARD_NO, APPROVED_NO
CNT = 0
CARD_NO = ""
APPROVED_NO = ""

def _getTest(card_no, approved_no):
    return dict(
                command_code = '01',
                initial_param = dict(
                                    card_no    =card_no,
                                    approved_no=approved_no,
                                    ),
                executer = 'addin.executer.refund_card.RefundCard'
            )

def run_flask_app():

    app = Flask(__name__)

    @app.get('/')
    def hello():
        global CNT
        global CARD_NO
        global APPROVED_NO
        CNT += 1
        print('CNT : ',CNT)
        if CNT % 5 != 0:
            return "Wait!!", status.HTTP_404_NOT_FOUND
        elif APPROVED_NO:
            dict_v = _getTest(CARD_NO, APPROVED_NO)
            APPROVED_NO = ""
            return dict_v, status.HTTP_200_OK
        else:
            return "No more refund!!", status.HTTP_404_NOT_FOUND
        
    @app.post('/purchase/')
    def post_purchase():

        params = json.loads(json.loads(request.get_data()))
        global CARD_NO
        global APPROVED_NO
        CARD_NO     = params['card_no']
        APPROVED_NO = params['approved_no']
        return {"message":"I recieved it!!!"}, status.HTTP_200_OK

    @app.put('/purchase/<approved_no>')
    def put_purchase(approved_no):
        params = json.loads(request.get_data())
        print('put_purchase approved_no : ', approved_no)
        print('put_purchase params : ', params)
        return {"message":"I recieved it!!!"}, status.HTTP_200_OK

    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8809, debug=True, use_reloader=False)).start()

if __name__ == '__main__':
    run_flask_app()
    print('printed?')