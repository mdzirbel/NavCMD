@echo off
cd C:\Users\matth\Documents\Programming Projects\CMD Navigation
py to.py %* > Output
SET /p dest=<Output
cd %dest%