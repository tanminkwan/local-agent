from miniagent.adapter import Adapter

class PrinterAdapter(Adapter):

    def print_image_file(self, param):        
        return 1, self.get_adaptee().printImageFile(param)

    def get_printer_info(self):
        return self.get_adaptee().getPrinterInfo()
    
    def release_printer(self):
        return self.get_adaptee().releasePrinter()
    
    def get_status(self) -> int:
        return self.get_adaptee().getPrinterStatus()