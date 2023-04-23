from app.executer import ExecuterInterface
from app.adapter_interface import PrinterAdapterInterface,\
      PaymentAdapterInterface, RESTServerAdapterInterface
from addin.dbquery.purchase_card_queries import update_purchase

class RefundCard(ExecuterInterface):

    def execute_command(self, 
                            initial_param: dict, 
                            payment: PaymentAdapterInterface,
                            restserver: RESTServerAdapterInterface,
                        ) -> tuple[int, dict]:
        
        print('initial_param : ', initial_param)

        # 1. Refund
        rtn, message = payment.refund_credit(
                            initial_param['card_no'],
                            initial_param['approved_no'])
        
        condition = dict(approved_no = initial_param['approved_no'])

        # 3. Db
        update_purchase(message, condition)

        # 4. Restserver 
        restserver.put_refund(
                      approved_no = initial_param['approved_no'],
                      refund_no   = message['refund_no'],
                      refund_date = message['refund_date'],
                    )
        
        return 1, dict(message="Well Done!!!!")
