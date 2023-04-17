
from importlib import import_module
from app.printer_adapter import PrinterAdapterInterface

class PrinterAdapter(PrinterAdapterInterface):

    def __init__(self):
        self._adaptee = None

    def set_adaptee(self, class_path: str):
        return self._create_adaptee(class_path)

    def _create_adaptee(self, class_path: str):

        package_name = '.'.join(class_path.split('.')[:-1])
        class_name = class_path.split('.')[-1]

        try:
            package_module = import_module(package_name)
        except ImportError:
            return -1, "'{}' is not imported.".format(package_name)
            
        if not hasattr(package_module, class_name):
            return -2, "module '{}' has no attribute '{}'"\
                            .format(package_name, class_name)
            
        class_obj = getattr(package_module, class_name)
        self._adaptee = class_obj()
        return 1, "OK"

    def print_image_file(self, param):
        self._adaptee.printImageFile(param)
        return 1, ""

    def get_printer_status(self):
        return self._adaptee.getPrinterStatus()

    def get_printer_info(self):
        return self._adaptee.getPrinterInfo()
    
    def release_printer(self):
        return self._adaptee.releasePrinter()