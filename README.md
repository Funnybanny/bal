#Useful tool for updating your main TM folder from your projects


Installation:

It was done by Pyinstaller (https://www.pyinstaller.org/) using 'pyinstaller --onefile script.py'.

To run:

Dist folder holds .exe and config.ini file. 
Simply change paths in config.ini along with the files extension then simply run .exe

-----------------------------------------------------



Simple Python Script for copying files. This was specificly made for OmegaT (http://omegat.org/).
The script compares given file type in project and CTM folder. If file in project folder has been modified since last modified of file in CTM folder with same name the script updates file in CTM folder (and also does it in Auto folder). If copy of file doesnt exists in CTM makes a copy of it (and also does it in Auto folder).
Open Config.ini to change paths to project folders.

[Folder]

project= where you keep your projects

CTM and Auto are for OmegaT folders

[Extension]

primary= type of file (for OmegaT purposes leave it .tmx)

