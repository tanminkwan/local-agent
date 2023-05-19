import requests
import uuid
import json
from datetime import datetime
from miniagent.flask_zipkin import child_zipkin_span

class CardPrinterAdaptee:

    def printImageFile(self, param):
        return 'CardPrinterAdaptee.printImageFile called : ' + param

    def getPrinterStatus(self):
        return 1

    def getPrinterInfo(self):
        return 'Smart-52 card printer'

class CreditCardPaymentAdaptee:

    def approveCredit(self, card_no, payment_amount):
        return 1, dict(
                    card_no=card_no,
                    payment_amount=payment_amount,
                    approved_no=uuid.uuid4().hex,
                    approved_date=datetime.now()
                    )

    def refundCredit(self, card_no, payment_amount):
        return 1, dict(
                    refund_no='RF_'+uuid.uuid4().hex[3:],
                    refund_date=datetime.now()
                    )

class RESTServer:

    def postPurchase(self,
                    product_code: str,
                    card_no: str, 
                    payment_amount: int,
                    approved_no: str,
                    approved_date: datetime, 
                    ) -> tuple[int, dict]:
        
        post_data =dict(
                        product_code  = product_code,
                        card_no       = card_no, 
                        payment_amount = payment_amount,
                        approved_no   = approved_no,
                        approved_date = approved_date.isoformat()
                    )

        try:

            with child_zipkin_span('postPurchase') as span:
                headers = {}
                headers.update(span.create_http_headers_for_new_span())
                response = requests.post("http://localhost:8809/purchase", json=json.dumps(post_data), headers=headers, timeout=10)
                span.update_tags(url=response.url, data=post_data)

        except ConnectionError as e:
            return -1, {"message":"ConnectionError to http://localhost:8809/purchase"}

        return 1, response.json()
    
    def putPurchase(self,
                    approved_no: str,
                    refund_no: str,
                    refund_date: datetime, 
                    ) -> tuple[int, dict]:
        
        put_data =dict(
                        refund_no   = refund_no,
                        refund_date = refund_date.isoformat()
                    )
        response = requests.put("http://localhost:8809/purchase/"+approved_no, json=json.dumps(put_data), timeout=10)
        return 1, response.json()
    
