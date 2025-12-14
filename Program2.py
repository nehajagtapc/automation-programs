'''Python Automation : In this script,renaming the file in a specific directory.'''

import sys
from sys import *
import os
from pathlib import Path


def main():
    print("---- Python Automation Script -----")

    print("Application name : " +argv[0])
    print("Directory is: "+argv[1])
    print("Extension1 is:"+argv[2])
    print("Extension2 is:"+argv[3])

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

    # Listing the files of a folder
    print("Before rename")
    files = os.listdir(source_folder)
    print(files)

    # rename each file one by one
    for file_name in files:
    # construct full file path
        old_name = os.path.join(source_folder, file_name)

    # Changing the extension from txt to pdf
        new_name = old_name.replace(argv[2], argv[3])
        os.rename(old_name, new_name)

    # print new names
    print("After rename")
    print(os.listdir(source_folder))

 
if __name__ == "__main__":
    main()