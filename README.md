Carbon Copy Cloner Remote Destination Cleaner


Carbon Copy Cloner doesn't provide the ability to purge the safetty net folder on remote backup destinations causing them to become very large and prevent backups if the disk runs out of space.

This script deletes folders that are 2 months old and are not from the last day of the month. This means that there is a archive of backups.

When you run it for the first time it will only delete the folders from 2 months ago so you will need to manually delete the others or change thescript. 

For the script to work the user running it needs read&write permissions for the _CCC SafetyNet folder and the folders within it.
