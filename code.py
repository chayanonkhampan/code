import random
import string
import time

def generate_random_code():
  x_chars = ".join(random.choices(ascii_uppercase + string.digits, k=16))
  code = f"RI-{x_chars[:4]}-{x_chars[4:8]}-{x_chars[8:12]}-{x_chars[12:16]}"
  return code
  def main():
    while True:
      random_code = generate_random_code()
      print(random_code)
      
      time.sleep(1)

if__name__=="__main__":
 main()
