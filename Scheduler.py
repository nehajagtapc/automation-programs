import time
import datetime
import schedule

def task():
	print("Task after each minute gets executed")
	print("Current time is: ",datetime.datetime.now())

def main():
	print("Inside main function")
	print("Schedule starts....")

	schedule.every(1).minutes.do(task)
		#drrr 1 minta ne task nav function tu run kr
	
	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == "__main__":
	main()

