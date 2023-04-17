import abc
from importlib import import_module
#from .common import SingletonInstane

# Factory class
class PrinterFactory:

    @staticmethod
    def create_adapter(class_path: str):

        package_name = '.'.join(class_path.split('.')[:-1])
        class_name = class_path.split('.')[-1]

        package_module = import_module(package_name)
        class_obj = getattr(package_module, class_name)
        
        return class_obj()
        
class PrinterAdapterInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'print_image_file') and 
                callable(subclass.print_image_file) and 
                hasattr(subclass, 'get_printer_status') and 
                callable(subclass.get_printer_status) and
                hasattr(subclass, 'get_printer_info') and 
                callable(subclass.get_printer_info) and
                hasattr(subclass, 'release_printer') and 
                callable(subclass.release_printer) or 
                NotImplemented)
    

