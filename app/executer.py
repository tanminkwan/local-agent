from .common import SingletonInstane
from .adapters import PrinterAdapter

class Executer(SingletonInstane):
  
    def __init__(self):
        pass

    def executeCommands(self, message: dict) -> dict:

        execution_steps = message['execution_steps']

        for step in execution_steps:
            
            if step['type'] == 'adaptee':

                adaptee_name = step['class_name']
                function_name = step['function_name']

                padapter = PrinterAdapter()
                #rtn, msg = padapter.setAdaptee('addin.tadaptee.tadaptee.CardPrinterAdaptee')
                adaptee_instance, rtn, msg = padapter.get_adaptee(adaptee_name)
                print(rtn, msg)

                if adaptee_instance:
                    func = getattr(adaptee_instance, function_name)
                    print(func())

        return 1, {}
    
    def test(self):
        return "This is TEST function."