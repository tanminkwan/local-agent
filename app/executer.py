from .common import SingletonInstane
from .printer_adapter import PrinterFactory

class Executer(SingletonInstane):
  
    def __init__(self):
        pass

    def executeCommands(self, message: dict) -> dict:

        execution_steps = message['execution_steps']

        for step in execution_steps:
            
            if step['type'] == 'adaptee':

                adapter_name = step['adapter']
                adaptee_name = step['class_name']
                function_name = step['function_name']

                padapter = PrinterFactory.create_adapter(adapter_name)
                #rtn, msg = padapter.setAdaptee('addin.tadaptee.tadaptee.CardPrinterAdaptee')
                rtn, msg = padapter.set_adaptee(adaptee_name)
                print(rtn, msg)

                func = getattr(padapter, function_name)
                print(func())

        return 1, {}
    
    def test(self):
        return "This is TEST function."