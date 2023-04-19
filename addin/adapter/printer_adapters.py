from app.adapter_interface import PrinterAdapterInterface

class PrinterAdapter(PrinterAdapterInterface):

    def print_image_file(self, param):
        self._adaptee.printImageFile(param)
        return 1, ""

    def get_printer_status(self):
        return self._adaptee.getPrinterStatus()

    def get_printer_info(self):
        return self._adaptee.getPrinterInfo()
    
    def release_printer(self):
        return self._adaptee.releasePrinter()