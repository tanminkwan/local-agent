import json
import sys
import os
from github import Github, Repository, ContentFile
import requests
from argparse import ArgumentParser, Namespace

def jsonFile2Dict(jsonFile: str) -> tuple[int, dict]:

  try:
    f = open(jsonFile)
    data = json.load(f)
  except FileNotFoundError as e:
    return -1, dict(error="JsonFile is not found : {}".format(jsonFile))
  except json.decoder.JSONDecodeError as e:
    return -2, dict(error="JSONDecodeError occured : {}".format(sys.exc_info()[1]))
  
  return 1, data

class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance
  
if __name__ == '__main__':
  rtn, message = jsonFile2Dict('test.json')
  print(rtn, message )

