# Assignment 4
This assignment allows the user to open an environemnt that is already setup and save out maya and fbx files based on the environment variables.
## Example Project Directory
This is an example of a project directory that can be created and will function with this assignment. You have to manually create your individual scene folders. Folders for your object, fbx, maya, and files will automatically be created with the script.
```
📁 Project
    ┗ 📁 scenes
        ┗ 📁 arctic
        ┗ 📁 attic
        ┗ 📁 desert
        ┗ 📁 global
            ┗ 📁 lamp
        ┗ 📁 jungle
            ┗ 📁 gorilla_statue
        ┗ 📁 volcano
```
## Environment Function and Use(Git Bash)

In the aliases.sh folder, genereall located at "C:\Program Files\Git\etc\profile.d\aliases.sh", paste in the following function and alias that set up your environment and easily open maya in the environment.
```bash
alias maya='/c/Program\ Files/Autodesk/Maya2025/bin/maya.exe' #path to your maya.exe file

scene() {
	export SCENE="$1"
	export OBJECT="$2"
    export TASK="$3"
	export USER="$4"

	export PROJECT_DIR=/c/Project/scenes/"$SCENE" #path to your project directory with '/"$SCENE"' at the end this uses the example directory provided
	echo Setting project to "$PROJECT_DIR"
	cd "$PROJECT_DIR"
	export MAYA_PROJECT="$PROJECT_DIR"

}
```
To use this, open a Git Bash terminal. To open an environment you will go type in "scene scenename objectname task user" making sure that you have a folder for the object inside your scene in your project directory.

Examples:
``` 
scene global lamp anim nj399

scene jungle gorilla_statue model nj399
```
After opening your environment you will want to run maya by entering "maya" into get bash. Once maya opens you can create a new file or open an exsisting file in your project directory

Note: If you are opening an exsisting file just make sure you are opening a file within the environment you just opened

From here you can work on your project and use the script when needed.

## Python Script for Maya
This script will save out a .ma file and export a .fbx file from maya with into folders and with naming based on your environment. The fbx file exports the selected objects if nothing is selected it will export the full scene.

Use the script "midterm.py" located in the python folder. You can either run this script using script editor, or create a shelf button that will run the script. An easy way to create a shelf button is to copy the python code into a python script editor. Select all the code in the script editor and then click and drag it to your shelf, make sure you select python, and it will add the button for you(It is easier if you also make the necisarry adjustments below before this step).

You may need to update the script on line 11 so that the file path is where the fbx.settings.json file is located. This script will print to the console your file location or some help to errors you may run into based on environment issues.

You can change the fbx export settings used by updating the fbx.settings.json file located in the config folder.

## Troubleshooting

### Can't find exported/saved files
Check the maya log, the script will print out the path to the files.

### Files not saving to correct location or at all
Double check your git bash aliases.sh file has been updated to correctly for the PROJECT_DIR variable. The formatting is not the same as python you can drag and drop the folder you want the path to in a git bash terminal to copy correct formatting.