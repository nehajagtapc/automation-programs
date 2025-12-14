'''Python Automation: In this script, finding the duplicate files
   deleting all duplicate files and create a log folder and then this log log file is
   send to  a specific mail id '''

import sys
from sys import *
import os
from pathlib import Path
import time
import hashlib
import psutil

#Delete the duplicate files
def DeleteFiles(dict1):
    
    results = list(filter(lambda x: len(x)>1,dict1.values()))

    icnt = 0
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("No duplicate files found")

 
def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

#Finding duplicate files and removing 
def findDup(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups

    else:
        print("Invalid Path")

#Finding duplicate result
def printResults(dict1):
    results = list(filter(lambda x: len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates found")
        print("The following files are duplicate")
        for  result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
    else:
        print("No duplicate files found")

#Finding path and Duplicate files 
def ProcessMemory(dict1,log_dir="Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separtor = "-" * 80
    log_path =os.path.join(log_dir,"Marvellous")    
    f= open(log_path,'w')   
    f.write(separtor+"\n")  
    f.write("Process Logger " +time.ctime()+ "\n")
    f.write(separtor+"\n")

    results = list(filter(lambda x: len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates files are Sucessfully copied")
        for  result in results:
            for subresult in result:
                print("\t\t%s"%subresult)
                listprocess.append(subresult)
    else:
        print("No duplicate files found")

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    print("---- Python Automation Script -----")

    print("Application name : " +argv[0])
    print("Directory is: "+argv[1])
    print("File created : "+argv[2])
    
    
    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[2] == "-h") or (argv[2] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[2] == "-u") or (argv[2] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    cwd = os.getcwd() # Print the current working  directory
    print("Current working directory:")
    print(cwd)

    print(cwd+"\\"+argv[1])
    source_folder = cwd+"\\"+argv[1]

    arr={}
    startTime = time.time()
    arr = findDup(argv[1])
    printResults(arr)
    DeleteFiles(arr)
    ProcessMemory(arr,argv[2])
    endTime = time.time()

    print("Took %s seconds to evaluate "%(endTime - startTime))
    
if __name__ == "__main__":
    main()