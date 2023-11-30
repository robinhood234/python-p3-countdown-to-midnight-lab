# your code goes here!
import time

def countdown(count = 10):
  while count > 0:
    print(f"{count} SECOND(S)!")
    count -= 1
    print("HAPPY NEW YEAR!")



   def countdown_with_sleep(count = 10):
     while count > 0:
      print(f"{count} SECOND(S)!")
      time.sleep(1)
      count -= 1
      print("HAPPY NEW YEAR!")