#!usr/bin/python3

from os import confstr
import sys
import re
from re import X, findall, search
from typing import Coroutine, Counter
from heapq import nlargest 
from prettytable import PrettyTable
import os 


class fun:
    find_string=""
    filename=""
    ip_address= ""
    event_no =[]
    counter=1
    line_number=[]
    count=0
    ipdst=[]
    ipsrc=[]
    dstport=[]
    attackip=[]
    attackdst=[]
    attackport=[]
    attacktype=[]


class servers:
    name=''
    def services(x):

        if int(x) ==80:
            name= 'Hypertext Transfer Protocol'
            return name
        if int(x) == 8080:
            name= "TCP/UDP"
            return name
        if int(x)== 8000:
            name="Seafile Windows Server (TCP)"
            return name
        else:
            name=" undefined "
            return name


def tables():
    x = PrettyTable()
    x.field_names = ["Ip source Addesses","Ip dst Addesses", " dst Ports","Services", "Kind of Attacks", "Attack examples","Total Attacks"]
    print("Printing Report...")
    for i in range(3):
        x.add_row([fun.attackip[i],fun.attackdst[i],fun.attackport[i] , servers.services(fun.attackport[i]),fun.filename, fun.attacktype[i][5:100],fun.count])
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
    kindOfAttack(int(input()))

    
    
# few attack types
 
def kindOfAttack(x):
    find=''
    print ("Encoding the Input...")
    if x ==1:
        lfi= "/../../"
        fun.filename= "Local_file_inclusion_(LFI)"  # create a "summary file" 
        find = lfi
    elif x ==2 :
        rfi= "/?="
        fun.filename= "Remote File Inclusion (RFI)"    # modfi "summary file"
        find = rfi
    elif x ==3 :
        buffr= r"(\\x\D)"
        find = buffr
        fun.filename= "Buffer OverFlow Attack (BOF)"   # modify "summary file"
    elif x ==4:
        i =0
        for i in range(3):
            i += 1
            x =i
            print(i) 
            # kindOfAttack(readfile())
            break
        

    else:
        print ("dont be stupid !!!!!!")
        exit()
    

    fun.find_string = find
    print(fun.filename)
    readfile()
   
def sysarg(x):
    print(f"Finding {x}...")
    readfile()

# Import data from log file
def readfile():

    attack_source=[]
    attack_dst=[]
    attack_dstPort=[]
    attack_type=[]
    attack_type= []
    print ("Opening the log file....")
    f = open("/home/kali/Documents/project/http1.log", "r")
    # counter=0
    file = f.readlines()
    # print(file[9])
    # data=[]
    print ("Reading the log file....")
    linenumbercounter=0
    for line in file:
        # if fewlines < 11:
        linenumbercounter+=1
        if re.search(fun.find_string, str(line)):
            fun.count+=1
            fun.line_number.append(linenumbercounter)

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
    makefile()
    print ("Parsing the data...")
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

    print("Creating a file...")

    ipsrcfile = open(fun.filename, "a+")
    ipsrcfile.write("\n"+ str(fun.line_number))
    ipsrcfile.close() 
    print("File created. Closing it now")

if len(sys.argv) > 1 :
    
    sysarg(sys.argv[1])

else:
    userinput()
    # makefile(fun.ipdst)
    # print ("working on Bash now...........")
    # os.system("./bash")
    tables()
    print(color.BOLD+f"\n\n\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n\n")


