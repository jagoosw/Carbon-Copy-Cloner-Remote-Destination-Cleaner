"""
    Carbon Copy Cloner Safety Net Cleaner for Remote Backup Destination
    ~~~~~~~~~
    Created on the 3rd of June 2016 by Jago Strong-Wright
    ~~~~~~~~
    Carbon Copy Cloner doesn't provide the ability to purge the safetty net 
    folder on remote backup destinations causing them to become very large 
    and prevent backups if the disk runs out of space.

    This script deletes folders that are 2 months old and are not from the 
    last day of the month. This means that there is a archive of backups.

    When you run it for the first time it will only delete the folders from 
    2 months ago so you will need to manually delete the others or change the
    script. 

    For the script to work the user running it needs read&write permissions
    for the _CCC SafetyNet folder and the folders within it

"""

#Used to delete the folderrs
import shutil

#Used to list the content of _CCC SafetyNet
import os

#Used to find current date 
import datetime

#Used to find the length of months
import calendar

#In function so accessible from automateRun.py
#path is the full path to _CCC SafetyNet - e.g. "/Volumes/Backup/_CCC SafetyNet"
def prunePath(path):
	
	#Lists contenct of folder
	pathAllFiles = os.listdir(path)

	#Finds the age of folders to delete	
	maxMonth = str(datetime.datetime.now().month - 2)
	#In number version to find length of month
	maxMonthInt = datetime.datetime.now().month - 2
	#When finding files to delete used so that files with the max month in the time are not also deleted (e.g. file could be called 2016-05-21 ... 21-04-36 which would be found in an april search due to the time of the backup (21-04-36))
	currentYear = str(datetime.datetime.now().year)

	#Initiate list of 
	deleteFoulders = list()

	if len(maxMonth) < 2:
		#Formats the month so it is as the folder is
		maxMonth = "0" + maxMonth
		
	#Cycles through the safety net folder looking for 2 month old olders	
	for folder in pathAllFiles:
		#Check if the folder is the right age
		if currentYear+"-"+maxMonth+"-" in folder:
			#Checks that its not the last one of the month
			if currentYear+"-"+maxMonth+"-"+str(calendar.monthrange(datetime.datetime.now().year, maxMonthInt)[1]) not in folder:
				#Deletes the folder
				shutil.rmtree(path+"/"+folder)

	#Tells you its finished for that run			
	print("Complete clean for path: ", path)
