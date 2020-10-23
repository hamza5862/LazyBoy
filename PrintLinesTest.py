#!usr/bin/python3

#from os import confstr
import sys
import re
from re import X, findall, search
from typing import Coroutine, Counter
from heapq import nlargest
from prettytable import PrettyTable
import os


class fun:
    doc=""
    find_string=""
    filename=""
    ip_address= ""
    event_no =[]
    counter=1
    line_number=[]
    find=''
    count=0
    ipdst=[]
    ipsrc=[]
    dstport=[]
    attackip=[]
    attackdst=[]
    attackport=[]
    attacktype=[]
    full_line= []
    linenumbercounter=0
    x=0




class servers:
    name=''
    def services(x):

        if int(x) ==80:
            name= 'Hypertext Transfer Protocol'
            return name
        elif int(x) == 8080:
            name= "TCP/UDP"
            return name
        elif int(x)== 8000:
            name="Seafile Windows Server (TCP)"
            return name
        elif int(x)== 3128:
            name="TCP/UDP"
            return name
        else:
            name=" undefined "
            return name


def tables():
    x = PrettyTable()
    x.field_names = ["Ip source Addesses","Ip dst Addesses", " dst Ports","Services", "Kind of Attacks", "Attack examples","Total Attacks"]
    print(f"Printing Report...\n {fun.filename}")
    # for i in range(3):
    x.add_row([fun.attackip[0],fun.attackdst[0],fun.attackport[0] , servers.services(fun.attackport[0]),fun.filename, fun.attacktype[0][0:1000],' '])
    x.add_row([fun.attackip[1],fun.attackdst[1],fun.attackport[1] , servers.services(fun.attackport[1]),fun.filename, fun.attacktype[1][0:1000],fun.count])
    x.add_row([fun.attackip[2],fun.attackdst[2],fun.attackport[2] , servers.services(fun.attackport[2]),fun.filename, fun.attacktype[2][0:1000],' '])
    print(x)






class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#User input def
def userinput():
    # print(len(sys.argv))
    print("What kind of attack are you looking for? \n i.e: (1)LFI   -  (2)RFI - (3)BufferOverflow (4)All kind of attacks\n\n please input your chooice here: " )
    print("input recived...")
    # if int(input()) <
    pickattack(int(input()))


def pickattack(x):
    if x == 4:
        for i in range(3):
            allattacks(i+1)
           # readfile()
    else:
        allattacks(x)

def allattacks(x):
        find=''
        if x ==1:
            lfi= "/../../"
            fun.filename= "Local_file_inclusion_(LFI)"  # create a "summary file"
            find = lfi
            readfile()
            print(fun.full_line[0])
            # tables()
            # makefile()
            print(color.BOLD+f"\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n")

        elif x ==2 :
            rfi= "/?="
            fun.filename= "Remote File Inclusion (RFI)"    # modfi "summary file"
            find = rfi
            readfile()
            tables()
            makefile()
            print(color.BOLD+f"\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n")

        elif x ==3 :
            buffr= r"(\\x\D)"
            find = buffr
            fun.filename= "Buffer OverFlow Attack (BOF)"   # modify "summary file"
            readfile()
            tables()
            makefile()
            print(color.BOLD+f"\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n")

        else:
            print ("dont be stupid !!!!!!")
            exit()
        fun.find_string = find

        # readfile()


##
# Import data from log file
def readfile():

    attack_source=[]
    attack_dst=[]
    attack_dstPort=[]
    attack_type=[]
    attack_type= []
    f = open(fun.doc, "r")
    # counter=0
    file = f.readlines()
    # print(file[9])
    # data=[]

    for line in file:
        # if fewlines < 11
        fun.linenumbercounter+=1
        if re.search(fun.find_string, str(line)):

            fun.line_number.append(fun.linenumbercounter)
            fun.full_line.append(line)
            #print(line)
            entry_details = re.split(r'\t+', str(line))
            attack_source.append(entry_details[2])
            attack_dst.append(entry_details[4])
            attack_dstPort.append(entry_details[5])
            attack_type.append(entry_details[9])


    def getcount():
        fun.attackip = word_count(attack_source)
        # fun.attackip = word_count(attack_source,x)
        fun.attackdst =word_count(attack_dst)
        fun.attackport = word_count(attack_dstPort)
        fun.attacktype = word_count(attack_type)
    # makefile()
    getcount()

def word_count(str):
    counts = dict()
    words = str

    for word in words:
        # print("count")
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    ThreeHighest = nlargest(3, counts, key = counts.get)
    return ThreeHighest

    # for val in ThreeHighest:
    #     print(val, ":", counts.get(val))
    #     x = counts.get(val)
    #     return x

def attackcount(str):
    counts = dict()
    words = str

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    ThreeHighest = nlargest(3, counts, key = counts.get)
    for val in ThreeHighest:
        return str(counts.get(val))


def makefile():
    ipsrcfile = open(fun.filename, "a+")
    for fun.x in range(100):
        # print("looptest")
        ipsrcfile.write("\n\n" + str(fun.line_number[fun.x])+ '\n\n' + str(fun.full_line[fun.x]) + "\n\n")
    ipsrcfile.close()


if len(sys.argv) > 1 :

    fun.doc=str(sys.argv[1])
    print(sys.argv[0])


else:
    fun.doc="http1.log"


userinput()
