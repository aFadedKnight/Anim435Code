# anim435-2024
Assignments for class

## Assignment 3
Make building in maya using batch mode

### Use

Update file path for save file on line 43
```python
maya.cmds.file(rename=r"insert\your\path\here.mb")
maya.cmds.file(save=True)
```

Run maya in batch mode

Using git bash, create an alias to make use easier 
```bash
alias mayapy="winpty C:/Program\ Files/Autodesk/Maya202X/bin/mayapy.exe"
```

Run assignment3/py with mayapy
```bash
mayapy "C:\path\to\the\code\anim-435-2024-nj399\assignment3\bin\assignment3.py" --floors 3
```

You can pass through an argument for the number of floors that are desired using "--floors" or "-f" with the number of floors after it at the end, as shown in the example above

When this code is run it will save the file to the location that you set in the code as a maya binary file. You can open this file using maya to see the building created.

If you run this code multiple times it will overwrite your previous file so be sure to rename your file if you want to keep it before running again.