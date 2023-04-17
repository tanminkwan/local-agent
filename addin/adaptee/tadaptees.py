class CardPrinterAdaptee:

    def printImageFile(self, param):
        print('CardPrinterAdaptee.printImageFile called : ',param)

    def getPrinterStatus(self):
        return 'Very Good'

    def getPrinterInfo(self):
        return 'Smart-52 card printer'

class PrinterAdaptee:

    def printImageFile(self, param):
        print('PrinterAdaptee.printImageFile called : ',param)

    def getPrinterStatus(self):
        return 'Very Good'

    def getPrinterInfo(self):
        return 'Normal printer'

class PdfPrinterAdaptee:

    def printImageFile(self, param):
        print('PdfPrinterAdaptee.printImageFile called : ',param)

    def getPrinterStatus(self):
        return 'Very Good'