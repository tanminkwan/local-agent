from app.adapter_interface import PaymentAdapterInterface

class PaymentAdapter(PaymentAdapterInterface):

    def approve_credit(self, card_no: str, payment_amout: int) -> tuple[int, dict]:
        rtn, message = self._adaptee.approveCredit(card_no, payment_amout)
        return rtn, message