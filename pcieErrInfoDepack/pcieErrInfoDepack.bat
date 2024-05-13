@echo off


for /r %%f in (*.txt) do del %%f

python fileStrSortProc.py "PFI 0 PRINTF" ": msg=0x" 0

python fileStrSortProc.py "PFI 1 PRINTF" ": msg=0x" 1

python fileStrSortProc.py "PFI 12 PRINTF" ": msg=0x" 12

pause