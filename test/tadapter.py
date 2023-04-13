import abc
from common import SingletonInstane

class PrinterAdapteeInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'printImageFile') and 
                callable(subclass.printImageFile) and 
                hasattr(subclass, 'getPrinterStatus') and 
                callable(subclass.getPrinterStatus) and
                hasattr(subclass, 'getPrinterInfo') and 
                callable(subclass.getPrinterInfo) or 
                NotImplemented)
    
class PrinterAdapter(SingletonInstane):

    def __init__(self):
        self._adaptees = {}
        self._classInstance = None
        print('PrinterAdapter.__init__')

    def setAdaptee(self, className) -> None:
        if self._adaptees.get(className):
            print(className+' adaptees exists')
            self._classInstance = self._adaptees[className]
        else:
            classInstance = globals()[className]()
            if not isinstance(classInstance, PrinterAdapteeInterface):
                raise TypeError("Expected object of type PrinterAdapteeInterface, got {}".
                            format(type(classInstance).__name__))
            self._adaptees.update({className:classInstance})
            self._classInstance = classInstance
        return 1, ""

    def releaseAdaptee(self):
        self._classInstance = None
        return 1, ""

    def printImageFile(self, param):
        self._classInstance.printImageFile(param)
        return 1, ""

    def getPrinterStatus(self):
        return self._classInstance.getPrinterStatus()

    def getPrinterInfo(self):
        return self._classInstance.getPrinterInfo()

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