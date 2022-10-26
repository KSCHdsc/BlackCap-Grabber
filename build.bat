@echo off
color 0a
echo.
set /p a="Enter the exe name : "
if [%a%]==[] ( 
    CALL:error
    pause
    EXIT /B
) 
if [%a%] NEQ [] (
    CALL:main
    EXIT /B 1 
)
ECHO is on
:main
echo.
echo Name is: %a%
pyinstaller --clean --key BLACKCAP --onefile --noconsole -i NONE -n %a% index.py
rmdir /s /q __pycache__
rmdir /s /q build
del /f / s /q %a%.spec
echo.
echo generated exe as %a%.exe
EXIT /B 1 
ECHO is on
:error
echo.
echo bro enter a name
EXIT /B 1
