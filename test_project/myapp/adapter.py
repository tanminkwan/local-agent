from miniagent.adapter import Adapter

class TestAdapterWithAdaptee(Adapter):

    def test_function(self, param):        
        return 1, self._adaptee.testFunction(param)
    
    def get_status(self) -> int:
        return self._adaptee.getStatus()
    
class TestAdapterNoAdaptee(Adapter):

    def test_function(self, param):        
        return 1, 'param : {}'.format(param)
    
    def get_status(self) -> int:
        return 1