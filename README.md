# To add here. 

- what it does.

-files you would need.

>how to install

#h1for Windows

-visual studio code would work fine. 

-If you dont have it you can go to python.org/downlaods

 -Downlaod the latest python, its a lightweight software. should work for system32 as well. 
 
 - Need to install prettytbales() in windows
 - go to this link https://pypi.org/project/prettytable/

 

  -*install prettytables() module* 
   
   -`$pip install pretty table`
   
   -`$python -m pip install --upgrade pip`

-for better experince:
   
   -terminal size shoudl be 202x42


-how to use LazyBoy (withExamples)

LazyBoy is a convenient tool that takes web server logs (text files) and builds a data structure highlighting the types of attacks, the IP addresses affected, the source IP addresses all sorted in order based on occurences showing the user where the most attention is needed. LazyBoy also creates a file with the line numbers for all possible attacks so the user can manually investigate if needed. 

To use LazyBoy, you will need a log file in a certain format. 
  -With that file, you can feed it as an argument to the LazyBoy python file on the command line. 
  -You will receive a prompt, asking which kind of attack you are searching for. You may pick LFI, RFI, BUFFOVERFLOW or ALL. 
  -You will get a table as an output for that attack and the ip addresses with the most occurences.
  -There will be a file created in your folder, it will be named as the Type of attack you searched for.
