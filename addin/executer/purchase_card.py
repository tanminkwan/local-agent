from app.executer import ExecuterInterface
from app.adapter_interface import PrinterAdapterInterface, PaymentAdapterInterface


class PurchaseCard(ExecuterInterface):

    def execute_command(self, 
                            command_code: str, 
                            initial_param: dict, 
                            printer: PrinterAdapterInterface,
                            payment: PaymentAdapterInterface,
                            ) -> tuple[int, dict]:
        
        print('command_code  : ', command_code)
        print('initial_param : ', initial_param)
        print('printer.print_image_file : ', printer.print_image_file(initial_param['product_code']+'.jpg'))
        print('payment.approve_credit : ', 
              payment.approve_credit(
                initial_param['product_code'],
                initial_param['payment_amount'])
            )
        
        return 1, {}
