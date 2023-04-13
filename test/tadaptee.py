from tadapter import PrinterAdapter

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

if __name__ == '__main__':
    pAdapter = PrinterAdapter.instance()
    pAdapter.setAdaptee('PrinterAdaptee')
    pAdapter.printImageFile('From Adapter')
    print(pAdapter.getPrinterStatus())
    print(pAdapter.getPrinterInfo())
    pAdapter = PrinterAdapter.instance()
    pAdapter.setAdaptee('CardPrinterAdaptee')
    pAdapter.printImageFile('From Adapter')
    print(pAdapter.getPrinterStatus())
    print(pAdapter.getPrinterInfo())
    pAdapter.setAdaptee('PrinterAdaptee')
    pAdapter.printImageFile('From Kim')
    print(pAdapter.getPrinterStatus())
    print(pAdapter.getPrinterInfo())
    pAdapter.setAdaptee('PdfPrinterAdaptee')
    pAdapter.printImageFile('From Adapter')
    print(pAdapter.getPrinterStatus())