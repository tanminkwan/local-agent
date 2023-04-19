class CardPrinterAdaptee:

    def printImageFile(self, param):
        return 'CardPrinterAdaptee.printImageFile called : ' + param

    def getPrinterStatus(self):
        return 'Very Good'

    def getPrinterInfo(self):
        return 'Smart-52 card printer'

class CreditCardPaymentAdaptee:

    def approveCredit(self, card_no, payment_amount):
        return 1, "card_no : '{}' payment_amount : {} is approved.".format(card_no, payment_amount)