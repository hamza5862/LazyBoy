                                                               LazyBoy

This is a convenient python script users can use to filter Local File Inclusion, Remote File Inclusion and Buffer Overflow attacks from a HTTP log file all in one execution or one at a time. The tool builds a data structure highlighting the types of attacks, the IP addresses affected, the source IP addresses all sorted in order based on occurences showing the user where the most attention is needed. LazyBoy also creates a file with the line numbers for all possible attacks so the user can manually investigate if needed. 

==========================================================================================

PRE-REQUISITES

1) visual studio code (recommended) 
2) Python on command line to run code
   -If you dont have it you can go to python.org/downlaods

    -Downlaod the latest python, its a lightweight software. should work for system32 as well. 

    - Need to install prettytbales()
    - go to this link https://pypi.org/project/prettytable/

3) prettytables() module
   -*install prettytables() module* 
   -`$pip install pretty table  
   -`$python -m pip install --upgrade pip`

4) For the best experince terminal size shoudl be 202x42 (recommended)

===========================================================================================

COMMAND LINE/COMMAND PROMPT

./LazyBoy [logfile]

Example: ./LazyBoy [http.log]
 
   -- This will then create a file in your directory. The name will be the same as the attack you are searching for
   
   -- Example: Searching for a Local File Inclusion will generate a file named "Local File Inclusion"
   
   -- When you search for all attacks, you will have a file created for each of the attacks
    
