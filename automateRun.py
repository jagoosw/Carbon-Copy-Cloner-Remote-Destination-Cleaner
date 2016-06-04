

#Imports main cleaning file
import script

#Date time library for getting the time
import datetime

#Time Library for sleeping
import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Settings - the locations to clean - change this part - List full path to backup safetynet - e.g. /Volumes/Backup/_CCC SafetyNet
locations = ["/Volumes/Backup1/_CCC SafetyNet", "/Volumes/Backup2/_CCC SafetyNet"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#Infinite loop to make it run forever
while True:
	#Incase it doesn't work (e.g. permission error)
	try:
		#Waits untill the hour is 7am, will run at anytime in the hour depending on when you start it
		while "07:00" not in str(datetime.datetime.now()):
			print("Waiting until 7am")
			time.sleep(3300) 
		
		#Cleans each location
		for location in locations:
			script.prunePath(location)
		
		#Displays time of clean
		print("At: ", datetime.datetime.now())

	#If permission denied for folder shutil raises OSError, this statement catches it	
	except OSError as err:
		print("Looks like you don't have permission to modify that folder, change it with an administrators account and try again.  OS error: {0}".format(err))
	#If user exits with ^C exits and prevents it being caught by exceptions
	except KeyboardInterrupt as err:
		print("Goodbye then...")
		#Exits
		raise SystemExit
	#Catches other errors
	except:
		print("Unexpected error, oh well")
