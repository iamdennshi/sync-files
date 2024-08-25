import subprocess
import datetime
import sys
import os
import shutil
import re
from dirsync import sync
from config import paths


def main1(): 
  __DEBUG__ = True
  syncer_modes = ["from-andorid", "to-android", "local-dirs", "local-file"]

  def syncer(from_dir, to_dir, mode):
    if __DEBUG__ != True:
      if mode in syncer_modes:
        if mode == "from-andorid":
          subprocess.run(['adbsync', '--show-progress', 'pull', from_dir, to_dir])
        elif mode == "to-android":
          subprocess.run(['adb', 'push', '--sync', from_dir, to_dir], shell=True)
        elif mode == "local-dirs":
          sync(from_dir, to_dir, "sync", verbose=True, purge=True)
        elif mode == "local-file":
          # Если файл новый, то копируем
          if (os.path.getmtime(from_dir) > os.path.getmtime(to_dir)):
            shutil.copy2(from_dir, to_dir)
      else:
        raise Exception(f"Invalid mode - {mode}\n\tAvailable modes: {syncer_modes}")


  def sync_music():
    print('sync_music')
    
    FROM = 'E:/Music/'
    TO = '/storage/7D41-16F9/'
    print(f"Music >>> {FROM} -> {TO}")
    syncer(FROM, TO, "to-android")


  def sync_camera():
    print('sync_camera')
    STR_TODAY = datetime.datetime.today().strftime('%d-%m-%Y')

    FROM = '/storage/emulated/0/DCIM/Camera/'
    TO = f'C:/Users/den/test/{STR_TODAY}/'
    print(f"Camera >>> {FROM} -> {TO}")
    syncer(FROM, TO, "from-andorid")

    FROM = '/storage/emulated/0/DCIM/QuickVideoRecorder/'
    TO = f'C:/Users/den/test/{STR_TODAY}/'
    print(f"QuickVideoRecorder >>> {FROM} -> {TO}")
    syncer(FROM, TO, "from-andorid")

  def sync_files():
    print('sync_files')

    FROM="D:/ДИПЛОМ/"
    TO="E:/other/ПГАТУ/бакалавр/ДИПЛОМ/"
    print(f"Диплом >>> {FROM} -> {TO}")
    syncer(FROM, TO, "local-dirs")


    FROM="D:/obsidian/"
    TO="E:/other/obsidian/"
    print(f"obsidian >>> {FROM} -> {TO}")
    syncer(FROM, TO, "local-dirs")

    # Нужно синхронизировать  один файл
    FROM="D:/passd.kdbx"
    TO="E:/other/passd.kdbx"
    print(f"passd.kdbx >>> {FROM} -> {TO}")
    syncer(FROM, TO, "local-file")



  modes = {
    "music": sync_music,
    "camera": sync_camera,
    "files": sync_files,
  }
  args = sys.argv[1:]

  if (args != []):
    for arg in args:
      if arg in modes:
        try:
          modes[arg]()
        except Exception:
          print(f"[EXCEPTION] {sys.exc_info()[1]}")
      else:
        print(f"[ERROR] Invalid mode - {arg}\n\tAvailable modes: {list(modes.keys())}")
  else:
    print(f"[ERROR] No mode specified \n\tAvailable modes: {list(modes.keys())}")

def main():
  DEBUG = True

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