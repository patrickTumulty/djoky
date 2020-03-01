# djoky
Djoky (Pronounced "jockey") is a simple python file organizer. 

External text file (example below), dictate where certain files should be automatically redirected to on your computer.
The first line of code means, if there is a .txt file located in your /Downloads folder, move it to /Downloads/MiscText

```
# ... = home directory 

# Downloads 
.../Downloads -> .txt   -> .../Downloads/MiscText
.../Downloads -> .pdf   -> .../Downloads/MiscPdf
.../Downloads -> .dmg   -> .../Downloads/DiscImage
.../Downloads -> .mp4   -> .../Downloads/MiscVideo
.../Downloads -> .mov   -> .../Downloads/MiscVideo

# Desktop 
.../Desktop   -> .py    -> .../Developer/pythonFiles

# Documents 
.../Documents -> .pages -> .../Documents/pagesFiles

```
