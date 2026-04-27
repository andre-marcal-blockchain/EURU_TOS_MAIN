@echo off
setlocal

for %%I in ("%~dp0..") do set "BASE=%%~fI"

if not exist "%BASE%\runtime\logs" mkdir "%BASE%\runtime\logs"

"C:\Users\andre\AppData\Local\Programs\Python\Python314\python.exe" "%BASE%\scripts\smoke_test.py" >> "%BASE%\runtime\logs\smoke_test_task.log" 2>&1

endlocal