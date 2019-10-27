<h1>Carbon Copy Cloner Remote Destination Cleaner</h1>

<h2>Information</h2>
Carbon Copy Cloner doesn't provide the ability to purge the safetty net folder on remote backup destinations causing them to become very large and prevent backups if the disk runs out of space.

This script deletes folders that are 2 months old and are not from the last day of the month. This means that there is a archive of backups.

When you run it for the first time it will only delete the folders from 2 months ago so you will need to manually delete the others or change thescript. 

For the script to work the user running it needs read&write permissions for the _CCC SafetyNet folder and the folders within it.

<h2>To use:</h2>
<ul>
<li>Make sure the user running the script has read&write permission for the destination folder</li>
<li>Run from terminal - use the command python main.py fromt he folder that it is in</li>
<li>If you leave it running it should check the folder at 7am every day</li>
</ul>

<h2>Notes/Thoughts</h2>
<ul>
<li>I understand that this isn't the most efficent way to do something everyday it was just the easiest to make - I intend to make it more effiecent in the future</li>
<li>There are probably also better ways of keeping something running instead of having a terminal window open all the time too - I also intend to change this</li>
<li>It does need to be run on the remote Mac so you would need access to it to set it up</li>
</ul> 
<p></p>
