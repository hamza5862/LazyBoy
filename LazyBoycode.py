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
    
    # line_number=[]
    find=''
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
    # for i in range(3):

    x.add_row([fun.attackip[0],fun.attackdst[0],fun.attackport[0] , servers.services(fun.attackport[0]),fun.filename, fun.attacktype[0][:],' '])
    x.add_row([fun.attackip[1],fun.attackdst[1],fun.attackport[1] , servers.services(fun.attackport[1]),fun.filename, fun.attacktype[1][:],fun.count])
    x.add_row([fun.attackip[2],fun.attackdst[2],fun.attackport[2] , servers.services(fun.attackport[2]),fun.filename, fun.attacktype[2][0:10],' '])
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
    inputnumber=int(input())
    if inputnumber == 4:
        for i in range(3):
            temp = i+1
            kindOfAttack(temp)
            tables()
            print(color.BOLD+f"\n\n\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n\n")

    else:
        kindOfAttack(inputnumber)
        tables()
        print(color.BOLD+f"\n\n\n\n ********---->  Please look at file {fun.filename}.txt for line numbers.  <------********\n\n\n")

    
    

       
# few attack types
def kindOfAttack(x):
   print ("Encoding the Input...")

   if x ==1:
       lfi= "/../../"
       fun.filename= "Local_file_inclusion_(LFI)"  # create a "summary file" 
       fun.find = lfi
   elif x ==2 :
       rfi= "/?=http"
       fun.filename= "Remote File Inclusion (RFI)"    # modfi "summary file"
       fun.find = rfi
   elif x ==3 :
       buffr= r"(\\x\D)"
       fun.find = buffr
       fun.filename= "Buffer OverFlow Attack (BOF)"   # modify "summary file"    
   else:
       print ("dont be stupid !!!!!!")
       exit()
   print(fun.filename)
   readfile()
    



##

# Import data from log file
def readfile():

    attack_source=[]
    attack_dst=[]
    attack_dstPort=[]
    attack_type=[]
    attack_type= []
    print ("Opening the log file....")
    f = open(fun.doc, "r")
    counter=0
    file = f.readlines()
    print ("Reading the log file....")
    linenumbercounter=0
    line_number=[]
    ipsrcfile = open(fun.filename, "a+")
    for line in file:
        # if fewlines < 11:
        linenumbercounter+=1
        # if re.search(fun.find_string, str(line)):
        if re.search(fun.find, str(line)):
            fun.count+=1
            counter+=1
            line_number.append(linenumbercounter)

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
        # print(str(attack_type[0:100])+"\n\n")

    for i in range(counter):\
        ipsrcfile.write("\n LineNumber:"+ str(line_number[i])+"\nSource:"+str(attack_source[i]) + "\nDst Server:" + str(attack_dst[i])+ " -->  "+ str(attack_dstPort[i])+ "\nAttack:"+str(attack_type[i])+"\n\n\n")


        
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




if len(sys.argv) > 1 :

    fun.doc=str(sys.argv[1])
    print(sys.argv[0])


else:
    print
    print("else statemetn")
    fun.doc="http1.log"


userinput()

