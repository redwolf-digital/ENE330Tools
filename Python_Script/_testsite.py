"""
this python script required python version 3.10 or above
run this block for chack your python version

normally I'm write firmware in C for embedded device only I'm not expert Python and modern high-level computer language
some time you will find C writing style in this code and not have any OOP in this 
(Of course! generally micro-controller it not support OOP ;w;)

I hope someone can write it better than me and fork this project for make it better
thank you (OwO)b  

AUTHOR REDWOLF DiGiTAL [C.Worakan]
github : https://github.com/redwolf-digital


how to install python package (if not have of first install)
Windowns user :
    1. open CMD
    2. type
        - pip install numpy
        - pip install matplotlib
        - pip install telnetlib3

        
Linux user :
    1. open terminal :
    2. type
        - pip install numpy
        - pip install matplotlib
        - pip install telnetlib3
"""


class textColor :
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# system and module import
import platform
import threading

try :
    import numpy as np
    print(textColor.OKGREEN + "numpy -> OK" + textColor.ENDC)
except ImportError as e :
    print(textColor.FAIL + e," : NOT INSTALL!" + textColor.ENDC)
    exit()

try :
    import matplotlib.pyplot as plt
    print(textColor.OKGREEN + "matplotlib -> OK" + textColor.ENDC)
except ImportError as e :
    print(textColor.FAIL + e," : NOT INSTALL!" + textColor.ENDC)
    exit()

try :
    import telnetlib
    print(textColor.OKGREEN + "telnetlib -> OK" + textColor.ENDC)
except ImportError as e :
    print(textColor.FAIL + e," : NOT INSTALL!" + textColor.ENDC)
    exit()   
    

print(textColor.OKCYAN + "current python version : ", platform.python_version() + textColor.ENDC, "\n")


import random   # Test only
import time


ipTable = {
        1 : "192.168.1.10",
        2 : "192.168.1.11",
        3 : "192.168.1.12",
        4 : "192.168.1.13",
        5 : "192.168.1.14",
}


max_buffsize = 1024

Net_connFlag = False

memTemp = np.array([])    # buffer for save dump memory data form SoCs.


# function
# function for connect to Cora board
def connectBoard(boardID, port = 7) :
    """
    this functions used for connect to network
    return  1 - when connect successful
            0 - when connect fail
    """

    ## code for connect TCP/IP
    if(boardID == 0) :
        telnetlib.Telnet(ipTable[0], 23, timeout=1000)

    else :
        telnetlib.Telnet(ipTable[boardID], port, timeout=1000)




# function for check in put is integer or not (I hate dynamic variable type ;w;)
def isInt(x) :
    try :
        int(x)
        return True
    except ValueError :
        return False


# print dashline UwU
def dashline() :
    print("--------------------------------------------")










#------------------------------------------------------------------------------------
#                                      main script
#------------------------------------------------------------------------------------
def boardConnect(Net_connFlag = False) :
    try :
        while Net_connFlag == False :
            global BoardTargetID 
            BoardTargetID = input("Command or Connect to board ID ?\n>> ")

            if isInt(BoardTargetID) == False :
                
                # list Board ID and Board IP
                if BoardTargetID == '-l' or BoardTargetID == 'list' :
                    dashline()
                    for i in range(len(ipTable)) :
                        print(f"[board ID] {i+1} IP : {ipTable[i+1]}")
                    dashline()
                # help
                elif BoardTargetID == "--h" or BoardTargetID == "help":
                        dashline()
                        print("--h or help\t Help menu\n-l or list\t Show all board list\n\n press \"Ctrl+C\" for exit program")
                        dashline()
                # Bro wrong command
                else :
                    print(textColor.FAIL + "COMMAND NOT FOUND OR INPUT INTEGER ONLY" + textColor.ENDC)
            else :
                if int(BoardTargetID) > 0 and int(BoardTargetID) <= 5 :
                    # connect internet here

                    print(textColor.WARNING + "----> PRESS \"Ctrl+C\" FOR EXIT PROGRAMS <----" + textColor.ENDC)
                    # set flag to 1 if connect succeed
                    Net_connFlag = True
                else :
                    print(textColor.FAIL + "OUT OF RANGE" + textColor.ENDC)

    except KeyboardInterrupt :
        print(textColor.FAIL + "ADIOS" + textColor.ENDC)
        raise SystemExit



# function for main task
def mainProcess(Net_connFlag = False) :
    while True :
        try :
            while Net_connFlag == True :
                print("main process")
                time.sleep(1)
        except KeyboardInterrupt :
            print(textColor.FAIL + "ADIOS" + textColor.ENDC)
            raise SystemExit
    
    # packetCounter = 0
    # while(Net_connFlag == True) :
    #         # required data from Cora board and put it in buffer
    #         memTemp = np.empty((0, 0))            # clear buffer


    #         # test case add data to buffer
    #         for i in range(max_buffsize) :
    #             n = int(random.randint(0, 65535))
    #             memTemp = np.append(memTemp, [n])

    #         packetCounter = packetCounter + 1
    #         print("Packet count : ", packetCounter)

    #         plt.clf()
    #         plt.title("Packet Count : " + str(packetCounter))
    #         plt.xlabel("smaple block")
    #         plt.ylabel("value of sample")
    #         plt.plot(memTemp)
    #         plt.pause(1)



#optimize python script     
if __name__ == "__main__" :
    task1 = threading.Thread(target= boardConnect, args=(Net_connFlag,))
    task2 = threading.Thread(target= mainProcess, args=(Net_connFlag,))

    task1.start()
    task2.start()

    task1.join()
    task2.join()
    
