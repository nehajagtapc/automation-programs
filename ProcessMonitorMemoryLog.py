import sys
from sys import *
import os
import time
import datetime
import psutil


def ProcessMemory(log_dir="Marvellous"):
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

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])
			vms = proc.memory_info().vms/(1024*1024)
			pinfo['vms'] = vms
			listprocess.append(pinfo)
		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass

	for element in listprocess:
		f.write("%s\n"%element)

def main():
	print("Automation by Python...")
	print("Application name : "+argv[0])

	if(len(argv)!=2):
		print("Error : Invalid number of Argument")
		exit()

	if(argv[1]=="-h") or (argv[1]=="-H"):
		print("This script is use to Log the record of runing process")
		exit()

	if(argv[1]=="-u") or(argv[1]=="-U"):
		print("Usage: Applicationname: AbsolutePath_of_Directory")
		exit()

	try:
		ProcessMemory(argv[1])

	except ValueError:
		print("Error : Invalid datatype input")

	except Exception as E:
		print("Error : Invalid input",E)


if __name__ == "__main__":
	main()