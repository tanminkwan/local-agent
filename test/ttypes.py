import inspect
import types
import sys
import abc

class Test1:
  def tprint(self):
    print('I am Test1.')

class Test11(Test1):
  def tprint(self):
    print('I am Test11.')

class Test2(metaclass=abc.ABCMeta):
  def func(self, cnt: int, hnd: Test1):
    self.arg = cnt
    print(cnt)

  @abc.abstractclassmethod
  def execute_command(self, command_code: str, initial_param: dict, 
                      *args, **kwargs):
    raise NotImplementedError
  
class Test3(Test2):
  def execute_command(self, command_code: str, initial_param: dict, 
                      test1: Test11):
    test1.tprint()
    
T = Test3()
sig = inspect.signature(T.execute_command)

for param in sig.parameters.values():
  if param.name not in ['command_code', 'initial_param']:
      print('Param : ', param.name, param.annotation, param.annotation.__name__, param.kind)
  
#for m in sys.modules:
#  print('module : ', m, type(m), sys.modules[m])