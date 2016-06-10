import script
import datetime
import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Settings - the locations to clean - change this part - List full path to backup safetynet - e.g. /Volumes/Backup/_CCC SafetyNet
locations = ["/Volumes/Backup1/_CCC SafetyNet", "/Volumes/Backup2/_CCC SafetyNet"]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#This keeps the program running forever although I'm sure there are more efficent ways to do this
while True:
	try:
		while "07:00" not in str(datetime.datetime.now()):
			print("Waiting until 7am")
			time.sleep(3300) 
		
		for location in locations:
			script.prunePath(location)
		
		print("At: ", datetime.datetime.now())

	except OSError as err:
		print("Looks like you don't have permission to modify that folder, change it with an administrators account and try again.  OS error: {0}".format(err))
	except KeyboardInterrupt as err:
		print("Goodbye then...")
		raise SystemExit
	except:
		print("Unexpected error, oh well")
