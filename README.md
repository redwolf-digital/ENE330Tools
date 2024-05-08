# ENE330Tools
repository software/script for ENE330 embedded system design

> [!CAUTION]
> I not warranty ***source code/software*** in this repo it can run perfectly
>
> If you find any bugs or any thing else I trust you can fix it by yourself :trollface:

## connectTool
**Request Python module**  
*make sure you install in your computer*
- numpy
- matplotlib
- telnetlib3  

### install Python Module
Windows and linux
```cli
pip install numpy
pip install matplotlib
pip install telnetlib3
```
### how to run script
for **Windows** used CMD, Terminal or Windows PowerShell or any terminal software
```cli
py .\connectTool.py
```
or
```cli
python .\connectTool.py
```
</br>

for **Linux** used Terminal
```cli
py connectTool.py
```
or
```cli
python connectTool.py
```
### command
| command | Descriptions |
| --- | --- |
| ``` --h or help ``` | Help command |
| ``` --l or list ``` | List all board ID and IP use in lab |
| ``` -cID <boardID> or connectID <boardID> ``` | connect to board target</br> __range 1-5__ |
| press "Ctrl+c" | Terminate program |

### Packet/protocol

| Header | Descriptions |
| --- | --- |
| ST | Start |
| SP | Stop |

| Format | ** ST,xx,xx,xx,xx,...,xx,xx,SP ** |
| --- | --- |
| Ex |ST,FFFFFF,F0001A,...,AD5900,SP |

send in string format ***not hex*** via Telent port 7 only</br>