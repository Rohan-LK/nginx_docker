#!/usr/bin/env python3

from datetime import datetime

def get_resp(inp):
  results = "App1 Input at: " +str(datetime.now())+ " is: " +inp.upper()
  return results

if __name__=="__main__":
  result = get_resp('test')
  print("APP1: ", result)