import abc
from importlib import import_module
from datetime import datetime
from .common import split_class_path

class AdapterFactory:

    @staticmethod
    def create_adapter(class_path: str):

        package_name, class_name = split_class_path(class_path)

        try:    
            package_module = import_module(package_name)
        except ImportError:
            return None

        class_obj = getattr(package_module, class_name)
        
        if not issubclass(class_obj, Adapter):
            return None

        class_instance = class_obj()
        class_instance.set_adapter_name(class_path)

        return class_instance

class Adapter(metaclass=abc.ABCMeta):
    
    def __init__(self):
        self._adaptee = None
        self.adapter_name = ""
        self.adaptee_name = ""

    def set_adapter_name(self, adapter_name: str):
        self.adapter_name = adapter_name

    def get_adapter_name(self):
        return self.adapter_name

    def get_adaptee_name(self):
        return self.adaptee_name

    def set_adaptee(self, class_path: str):
        return self._create_adaptee(class_path)

    def _create_adaptee(self, class_path: str):

        package_name, class_name = split_class_path(class_path)

        try:
            package_module = import_module(package_name)
        except ImportError:
            return -1, "'{}' is not imported.".format(package_name)
            
        if not hasattr(package_module, class_name):
            return -2, "module '{}' has no attribute '{}'"\
                            .format(package_name, class_name)
            
        class_obj = getattr(package_module, class_name)
        self._adaptee = class_obj()
        self.adaptee_name = class_path

        return 1, "OK"

class RESTServerAdapterInterface(Adapter):

    @abc.abstractmethod
    def post_purchase(self, 
                      product_code: str,
                      card_no: str, 
                      payment_amount: int,
                      approved_no: str,
                      approved_date: datetime, 
                      ) -> tuple[int, dict]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_status(self) -> int:
        raise NotImplementedError

class PrinterAdapterInterface(Adapter):

    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'print_image_file') and 
                callable(subclass.print_image_file) and 
                hasattr(subclass, 'get_status') and 
                callable(subclass.get_status) and
                hasattr(subclass, 'get_printer_info') and 
                callable(subclass.get_printer_info) and
                hasattr(subclass, 'release_printer') and 
                callable(subclass.release_printer) or 
                NotImplemented)
    """
    @abc.abstractmethod
    def print_image_file(self, file_path: str) -> tuple[int, dict]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_status(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_printer_info(self) -> tuple[int, dict]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def release_printer(self) -> tuple[int, dict]:
        raise NotImplementedError

class PaymentAdapterInterface(Adapter):

    @abc.abstractmethod
    def approve_credit(self, card_no: str, payment_amount: int) -> tuple[int, dict]:
        raise NotImplementedError

    @abc.abstractmethod
    def refund_credit(self, card_no: str, approved_no: str) -> tuple[int, dict]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_status(self) -> int:
        raise NotImplementedError
