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
# system and module import
import platform


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
    
print()
print("\n[SYSTEM] -> initialize done\n" + textColor.OKCYAN + "current python version : ", platform.python_version() + textColor.ENDC, "\n")


import random   # Test only


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
#                                      Variable
#------------------------------------------------------------------------------------

ipLUT = {
        0 : "192.168.1.52",
        1 : "192.168.1.10",
        2 : "192.168.1.11",
        3 : "192.168.1.12",
        4 : "192.168.1.13",
        5 : "192.168.1.14"
}

memTemp = np.array([])      # data is here



#------------------------------------------------------------------------------------
#                                      main script
#------------------------------------------------------------------------------------

def terminalInput() :
    return input(textColor.OKBLUE + ">> " + textColor.ENDC)


def mainProcess(dataArrIn, boardTargetID_t) :
    
    max_buffsize = 64
    
    # required data from Cora board and put it in buffer
    dataArrIn = np.empty((0, 0))            # clear buffer
    
    # Connect Telnet
    ip = ipLUT[boardTargetID_t]
    tn = telnetlib.Telnet(ip, 7, 1000) 
    tn.open(ip, 7, 1000)
    # Telnet SEND RTS code 
    tn.write(b'g')
    dataIn = tn.read_until(b"SP").decode('utf-8')

    print(f"[SYSTEM] -> OPERATOR REQ. ID {str(boardTargetID_t)} DONE")

    dataArr = np.char.split(dataIn, sep=",")
    dataArr = dataArr.tolist()
    
    if dataArr[len(dataArr)-1] == 'SP' :
        dataArrIn = [int(x, 16) for x in dataArr[1:len(dataArr)-1]]
        print(f"[SYSTEM] -> DUMP RAM :\n {str(dataArrIn)}")

        plt.clf()
        plt.title("Data of Board ID " + str(boardTargetID_t))
        plt.xlabel("sample")
        plt.ylabel("value of sample")
        plt.xlim([0, max_buffsize])
        
        plt.plot(dataArrIn)
        plt.pause(1)
    else :
        print("ERROR") 
    

def main() :
    global connComplet
    global boardTargetID
    
    connComplet = 0



    try :
        while connComplet == 0 :

            commandInput = terminalInput()
            comm_buff = commandInput.split(" ")
            
            if isInt(commandInput) == False :
                # list Board ID and Board IP
                if commandInput == '--l' or commandInput == 'list' :
                    dashline()
                    for i in range(len(ipLUT)) :
                        print(f"[board ID] {i} IP : {ipLUT[i]} @ PORT 7")
                    dashline()

                # help
                elif commandInput == "--h" or commandInput == "help" :
                        dashline()
                        print("--h or help\t\t\t Help menu\n--l or list\t\t\t Show all board list\n-cID <1-5> or connectID <1-5>\t connect to target board\n\n press \"Ctrl+C\" for exit program")
                        dashline()

                # Connect board
                elif comm_buff[0] == "-cID" or comm_buff[0] == "connectID" :
                    if isInt(comm_buff[1]) == True :
                        if int(comm_buff[1]) >= 0 and int(comm_buff[1]) <= 5 :
                            boardTargetID = int(comm_buff[1])
                            connComplet = 1
                            print(textColor.WARNING + "[SYSTEM] -> EXIT COMMAND MODE\n----> PRESS \"Ctrl+C\" FOR EXIT PROGRAMS <----" + textColor.ENDC)
                        else :
                            print(textColor.FAIL + "OUT OF RANGE" + textColor.ENDC)
                    else :
                        print(textColor.FAIL + "ERROR" + textColor.ENDC)

                # Bro wrong command
                else :
                    print(textColor.FAIL + "COMMAND NOT FOUND" + textColor.ENDC)

            else :
                print(textColor.FAIL + "COMMAND NOT FOUND" + textColor.ENDC)


        while connComplet == 1 :
            try :
                mainProcess(memTemp, boardTargetID)

                
            except KeyboardInterrupt :
                print(textColor.FAIL + "- Glory to Mankind -" + textColor.ENDC)
                raise SystemExit


    except KeyboardInterrupt :
        print(textColor.FAIL + "- Glory to Mankind -" + textColor.ENDC)
        raise SystemExit


#optimize python script     
if __name__ == "__main__" :
    main()
    

