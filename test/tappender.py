from common import SingletonInstane

class Appender(SingletonInstane):
  
  def __init__(self):
      self.called_cnt = 0
      print('Appender.__init__')

  def printUrJob(self, message):
      self.called_cnt += 1
      print('Appender message : ',message + '('+ str(self.called_cnt)+')')

appender = Appender.instance()

if __name__ == '__main__':
    c = Appender.instance()
    c.printUrJob('Hello!')
    d = Appender.instance()
    d.printUrJob('Hello2!')
