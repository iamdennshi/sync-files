import os
import re
from dotenv import load_dotenv
from dirsync import sync
from config import paths

def main():
  load_dotenv()
  DEBUG = os.getenv('DEBUGING') == 'True'

  for src, target in paths.items():
    # Если винда меняем / на \\
    if os.name == 'nt':
      src = re.sub(r'/', r'\\', src)
      target = re.sub(r'/', r'\\', target)

    print(src, "->", target)

    if not DEBUG:
      sync(src, target, "sync", verbose=True, purge=True)



if __name__ == "__main__":
  main()