from datetime import datetime
from miniagent.executer import ExecuterInterface
from myapp.adapter import TestAdapterWithAdaptee, TestAdapterNoAdaptee
from myapp.dbquery import add_all_adapters_health

class DeviceHealth(ExecuterInterface):

    def execute_command(self,
                            initial_param: dict,
                            test1: TestAdapterNoAdaptee,
                            test2: TestAdapterWithAdaptee,
                        ) -> tuple[int, dict]:
        
        checked_date = datetime.now()

        val_list = []
        for obj in [test1, test2]:
            val_dict = \
                dict(
                    adapter_name = obj.get_adapter_name(),
                    adaptee_name = obj.get_adaptee_name(),            
                    is_healthy = 'YES' if obj.get_status() else 'NO',
                    checked_date = checked_date
                )
            val_list.append(val_dict)

        add_all_adapters_health(val_list)

        return 1, dict(message="Well Done!!!!")