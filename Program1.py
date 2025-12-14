'''Python Automation : In this Script,Finding the path of directory of files,
   check the file by using command line argument ends with (.txt,.py,.doc.,etc)
   and display that files on screen.'''

from sys import *
import os
import glob

def main():
    print("---- Python Automation Script -----")

    print("Application name : " +argv[0])
    print("Directory is: "+argv[1])
    print("Extension is:"+argv[2])
    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[2] == "-h") or (argv[2] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[2] == "-u") or (argv[2] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        flag = os.path.isabs(argv[1])
        if flag == False:
            path = os.path.abspath(argv[1])

        exists = os.path.isdir(argv[1])
    
        if exists:
        
            for foldername, subfolder, filname in os.walk(argv[1]):
                print("Current folder is : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+" is :"+subf)

            for filen in filname:
                print("File inside "+foldername+" is : "+filen)
            print("----- The files from directory is -----")

            for file in filname:
                if(file.endswith(argv[2])):      
                    print(file)
            print(' ')

        else:
            print("Invalid Path")

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

 
if __name__ == "__main__":
    main()