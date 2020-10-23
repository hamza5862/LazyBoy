# To add here.

- what it does.
-files you would need.
- how to install
-how to use LazyBoy (withExamples)

LazyBoy is a convenient tool that takes web server logs (text files) and builds a data structure highlighting the types of attacks, the IP addresses affected, the source IP addresses all sorted in order based on occurences showing the user where the most attention is needed. LazyBoy also creates a file with the line numbers for all possible attacks so the user can manually investigate if needed. 

To use LazyBoy, you will need a log file in a certain format. 
  -With that file, you can feed it as an argument to the LazyBoy python file on the command line. 
  -You will receive a prompt, asking which kind of attack you are searching for. You may pick LFI, RFI, BUFFOVERFLOW or ALL. 
  -You will get a table as an output for that attack and the ip addresses with the most occurences.
  -There will be a file created in your folder, it will be named as the Type of attack you searched for.
