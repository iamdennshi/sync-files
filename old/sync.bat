@echo off
start "" "C:\platform-tools\adb.exe" devices
echo Try to run adb server
pause

set host="E:\Pictures\Camera"
set android="/storage/emulated/0/DCIM/Camera/"
adbsync.exe %host% %android% /h /v /i.inflight_lowres


set host="E:\Music\lyrics"
set android="/storage/7D41-16F9/Music/lyrics"
adbsync.exe %host% %android% /a /v /i.spotdl-cache
set host="E:\Music\nolyrics"
set android="/storage/7D41-16F9/Music/nolyrics"
adbsync.exe %host% %android% /a /v /i.spotdl-cache
pause

flash:

start "" "C:\platform-tools\adb.exe" kill-server