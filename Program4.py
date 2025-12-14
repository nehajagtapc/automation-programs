'''Python Automation: In this script,Copying the files with specific .extension in the new directory.'''

import sys
from sys import *
import os
from pathlib import Path
import shutil


def main():
    print("---- Python Automation Script -----")

    print("Application name : " +argv[0])
    print("First Directory is: "+argv[1])
    print("Second Directory is:"+argv[2])
    print("Extension is: "+argv[3])

    if (len(argv) != 4):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[2] == "-h") or (argv[2] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[2] == "-u") or (argv[2] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    for foldername, subfolder, filname in os.walk(argv[1]):
        print("Current folder is : "+foldername)

    for subf in subfolder:
        print("Sub folder of "+foldername+" is :"+subf)

    for filen in filname:
        print("File inside "+foldername+" is : "+filen)

    cwd = os.getcwd() # Print the current working  directory
    print("Current working directory:")
    print(cwd)

    print(cwd+"\\"+argv[1])
    source_folder = cwd+"\\"+argv[1]

    print(cwd+"\\"+argv[2])
    destination_folder = cwd+"\\"+argv[2]

    iret3 = os.mkdir(argv[2])
    print("Directory Created : ",argv[2])
    
    files=os.listdir(source_folder) # iterating over all the files in source directory
    for fname in files:        
    # copying the files to the
    # destination directory
        for file in filname:
            if(file.endswith(argv[3])):
                shutil.copy2(os.path.join(source_folder,file),destination_folder)      
            print(file)
            
            
    print("Copied files Successfully")
if __name__ == "__main__":
    main()