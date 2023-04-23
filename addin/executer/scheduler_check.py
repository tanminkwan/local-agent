from app.executer import ExecuterInterface
from app.adapter_interface import PrinterAdapterInterface,\
      PaymentAdapterInterface, RESTServerAdapterInterface
from addin.dbquery.purchase_card_queries import update_purchase

class CheckRefund(ExecuterInterface):

    def execute_command(self
                        ) -> tuple[int, dict]:
        
        return 1, dict(message="Well Done!!!!")
