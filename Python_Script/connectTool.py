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




import random   # Test only


ipTable = {
        1 : "192.168.1.10",
        2 : "192.168.1.11",
        3 : "192.168.1.12",
        4 : "192.168.1.13",
        5 : "192.168.1.14",
}


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


# function for main task
def mainProcess(connFlag, buffSize, temp) :
    packetCounter = 0
    while(connFlag == 1) :
            # required data from Cora board and put it in buffer
            temp = np.empty((0, 0))            # clear buffer


            # test case add data to buffer
            for i in range(buffSize) :
                n = int(random.randint(0, 65535))
                temp = np.append(temp, [n])

            packetCounter = packetCounter + 1
            print("Packet count : ", packetCounter)

            plt.clf()
            plt.title("Packet Count : " + str(packetCounter))
            plt.xlabel("smaple block")
            plt.ylabel("value of sample")
            plt.plot(temp)
            plt.pause(1)


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
def main() :
    print(textColor.OKCYAN + "current python version : ", platform.python_version() + textColor.ENDC, "\n")

    NET_PORT = 7
    Net_connFlag = 0
    max_buffsize = 130


    memTemp = np.array([])    # buffer for save dump memory data form SoCs.


    try :
        # conditions make sure no idiot one input the system doesn't need
        while(Net_connFlag == 0) :

            BoardTargetID = input("Command or Connect to board ID ?\n>> ")


            if isInt(BoardTargetID) == False :
                if  BoardTargetID == "-l" or BoardTargetID == "list" :
                    dashline()
                    for i in range(len(ipTable)) :
                        print(f"[board ID] {i+1} IP : {ipTable[i+1]}")
                    dashline()

                elif BoardTargetID == "--h" or BoardTargetID == "help":
                        dashline()
                        print("--h or help\t Help menu\n-l or list\t Show all board list\n\n press \"Ctrl+C\" for exit program")
                        dashline()
                else :
                    print(textColor.FAIL + "COMMAND NOT FOUND OR INPUT INTEGER ONLY" + textColor.ENDC)


            else :
                if int(BoardTargetID) > 0 and int(BoardTargetID) <= 5 :
                    # connect internet here





                    print(textColor.WARNING + "----> PRESS \"Ctrl+C\" FOR EXIT PROGRAMS <----" + textColor.ENDC)
                    # set flag to 1 if connect succeed
                    Net_connFlag = 1

                else :
                    print(textColor.FAIL + "OUT OF RANGE" + textColor.ENDC)
            

        



        # connect Cora board succeed
        # run main process
        mainProcess(Net_connFlag, max_buffsize, memTemp)

    
    except KeyboardInterrupt :
        print(textColor.FAIL + "ADIOS" + textColor.ENDC)
        raise SystemExit


#optimize python script     
if __name__ == "__main__" :
    main()
