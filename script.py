
import shutil
import os
import datetime
import calendar

#path is the full path to _CCC SafetyNet - e.g. "/Volumes/Backup/_CCC SafetyNet"
def prunePath(path):

	pathAllFiles = os.listdir(path)
	maxMonth = str(datetime.datetime.now().month - 2)
	maxMonthInt = datetime.datetime.now().month - 2
	currentYear = str(datetime.datetime.now().year)
	deleteFoulders = list()

	if len(maxMonth) < 2:
		maxMonth = "0" + maxMonth
		
	for folder in pathAllFiles:
		if currentYear+"-"+maxMonth+"-" in folder:
			if currentYear+"-"+maxMonth+"-"+str(calendar.monthrange(datetime.datetime.now().year, maxMonthInt)[1]) not in folder:
				shutil.rmtree(path+"/"+folder)

	print("Complete clean for path: ", path)
