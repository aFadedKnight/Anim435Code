# Final: Decimate Geometry
Decimate geometry inside a maya file to create different LODs

## Use

#### Command Prompt
Open a command prompt. You can then run the script using '"C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" "final.py" -f "c:/path/to/maya/file" -a half'. Make sure that you are using the path to your mayapy.exe as well as the path to your final.py file. Most likely the path used in the example will be where your mayapy is if using maya 2025(just change the 2025 to be your correct verison if not using 2025)

#### Git Bash
In the aliases.sh folder, genereall located at "C:\Program Files\Git\etc\profile.d\aliases.sh", paste in the following alias which will make it so you don't need type the entire path to mayapy evertime.
```bash
alias mayapy='/c/Program\ Files/Autodesk/Maya2025/bin/mayapy.exe' #path to your mayapy.exe file
```

Most likely the path used in the example will be where your mayapy is if using maya 2025(just change the 2025 to be your correct verison if not using 2025)

Open a Git Bash window. You can then run the script using 'mayapy "c:/path/to/final.py" -f "c:/path/to/maya/file" -a half'. Make sure that you are using the path to your final.py file.

### Arguments

#### file
--file or -f

Give the path to the maya file that you want to have decimated. This is also the same directory that the outup file will be saved to

#### amount
--amount or - a
Specify the amount that you want to decimate a file by. You can use the predertimined values or use a specific percentage that you want to decimate the model by.

Predeetrmined values:

"three-quarters": 75
"two-thirds": 66
"half": 50
"third": 33
"quarter": 25
"eigth": 13