from sys import *
import webbrowser
import re
from urllib.error import *
from urllib.request import *

def is_connencted():
    try:
        
        urlopen('http://google.com') #Python 3.x
        return True
    except:
        return False

def Find(string):
    url=re.findall('http:\/\/www.google.com\/',string)
    return url

def Web_Launcher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url=Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("----------Marvellous Infosystems Automations---------")
    print("Automation Script Started with name :",argv[0])

    if(len(argv)!=2):
        print("Error : Insufficient Arguments ")
        print("Use -h for help and use -u for usage of script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help : This script is used to perform ______")
        exit()
    
    try:
        connected=is_connencted()

        if connected:
            Web_Launcher(argv[1])
        else:
            print("Unable to connect internet")
    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid Input ",E)

if __name__=="__main__":
    main()
        





  

b=is_connencted()
print(b)