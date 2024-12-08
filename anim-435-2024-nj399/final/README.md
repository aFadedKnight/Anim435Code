# Final: Decimate Geometry
Decimate geometry inside a maya file to create different LODs

## Use

#### Command Prompt
Open a command prompt. You can then run the script using '"C:\Program Files\Autodesk\Maya2025\bin\mayapy.exe" "final.py" -f "c:/path/to/maya/file" -a half'. Make sure that you are using the path to your mayapy.exe as well as the path to your final.py file. Most likely the path used in the example will be where your mayapy is if using maya 2025(just change the 2025 to be your correct verison if not using 2025)

You can also pass through a mode argument when running the script using -m or --mode.

#### Git Bash
In the aliases.sh folder, genereall located at "C:\Program Files\Git\etc\profile.d\aliases.sh", paste in the following alias which will make it so you don't need type the entire path to mayapy evertime.
```bash
alias mayapy='/c/Program\ Files/Autodesk/Maya2025/bin/mayapy.exe' #path to your mayapy.exe file
```

Most likely the path used in the example will be where your mayapy is if using maya 2025(just change the 2025 to be your correct verison if not using 2025)

Open a Git Bash window. You can then run the script using 'mayapy "c:/path/to/final.py" -f "c:/path/to/maya/file" -a half'. Make sure that you are using the path to your final.py file.

You can also pass through a mode argument when running the script using -m or --mode.

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

#### mode
--mode or -m

Decide what mode you want to use to reduce your geometry. by default the preserve mode is used

**"preserve**
Using the preserve mode will be less accurate in reaching the desired reduction amount entered For example if you are reducing by 50 percent if there are 100 faces it may only reduce to 60+ faces. This methos will do a better job at preserving detail as well as keeping quads which better keeps the shape of your object. For instance a cube would remain a cube with likely 0 overlapping

**"decimate"**
Using the decimate mode will more accuratley reach the desired the reduction amount entered. For example if you are reducing by 50 percent if there are 100 faces it will reduce to almost if not exacly 50 faces. However this could lose more detail in the geometry and remove faces in an unwanted way such as breaking up hard edges. For instance a cube may no longer have all of it's hard edges and some geometry may overlap.