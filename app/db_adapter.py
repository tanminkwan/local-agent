import abc
from importlib import import_module
from .common import SingletonInstane

class DBAdapteeInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_session') and 
                callable(subclass.get_session) and 
                hasattr(subclass, 'execute_sql_stmt') and 
                callable(subclass.execute_sql_stmt) and
                hasattr(subclass, 'close_session') and 
                callable(subclass.close_session) and
                hasattr(subclass, 'release_instance') and 
                callable(subclass.release_instance) or 
                NotImplemented)
    
class DBAdapter(SingletonInstane):

    def __init__(self):
        self._adaptees = []

    def _in_adaptees(self, class_name):
        return False
    
    def get_adaptee(self, class_path) -> tuple[DBAdapteeInterface, int, str]:

        package_name = '.'.join(class_path.split('.')[:-1])
        class_name = class_path.split('.')[-1]

        if self._in_adaptees(class_name):
            classInstance = self._adaptees[class_name]
        else:
            package_module = import_module(package_name)
            
            if not hasattr(package_module, class_name):
                return None, -1, "module '{}' has no attribute '{}'"\
                            .format(package_name, class_name)
            
            class_obj = getattr(package_module, class_name)
            classInstance = class_obj()

            print("class name : ", type(classInstance).__name__)

            if not isinstance(classInstance, DBAdapteeInterface):
                return None, -2, "Expected object of type DBAdapteeInterface, got {}"\
                            .format(type(classInstance).__name__)
            
            self._adaptees.append(classInstance)

        return classInstance, 1, ""

    def release_adaptee(self, classInstance: DBAdapteeInterface):
        
        if classInstance in self._adaptees: 
            classInstance.release_instance()
            self._adaptees.remove(classInstance)
        else:
            pass

        return 1, ""

    def printImageFile(self, param):
        self._classInstance.printImageFile(param)
        return 1, ""

    def getPrinterStatus(self):
        return self._classInstance.getPrinterStatus()

    def getPrinterInfo(self):
        return self._classInstance.getPrinterInfo()
    