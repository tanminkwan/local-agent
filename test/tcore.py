import json
import os
import yaml
from common import SingletonInstane, jsonFile2Dict

class Executer(SingletonInstane):
  
  def __init__(self):
    self._applyDefaultPolicies()

  def applyPolicies(self, policy: dict):
    self._policy = policy
     
  def getPolicies(self) -> dict:
    return self._policy

  def _applyDefaultPolicies(self):
    policyFileName = 'policy.json'    
    rtn, policy = jsonFile2Dict(policyFileName)
    if rtn < 0:
      policy.update(is_policy=False)

    self.applyPolicies(policy)

  def _validatePolicies(self):
    return 1, {}
  
  def _checkYaml(yamlFile: str) -> tuple[bool, str]:
    
    if not os.path.isfile(yamlFile):
      return False, 'File is not found'
    
    return True, ""
  
  def _loadPolicies():
    pass
  
  def exeCommand(command: dict) -> tuple[int, dict]:
    return 1, {}
  
executer = Executer.instance()

if __name__ == '__main__':
    p = executer.getPolicies()
    print(p)