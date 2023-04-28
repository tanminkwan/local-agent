from datetime import datetime
from miniagent.executer import ExecuterInterface

class PrintParam(ExecuterInterface):

    def execute_command(self,
                            initial_param: dict,
                        ) -> tuple[int, dict]:
        
        print('Class name : ', self.__class__.__name__)
        print('initial_param : ', str(initial_param))

        return 1, dict(message="Well Done!!!!")