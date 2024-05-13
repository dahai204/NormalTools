@echo off

echo "SysLog Depack start..."

python syslogDepack.py  " mcycle=" "_pcieDump_total.txt"

python syslogDepack.py  "PC802_0 PFI 0 PRINTF: msg=" "_pcieDump_pfi0.txt"
python syslogDepack.py  "PC802_0 PFI 1 PRINTF: msg=" "_pcieDump_pfi1.txt"

echo "SysLog Depack end..."

pause
