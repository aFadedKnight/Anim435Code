'''
This script will save a maya file and name it based on the environment. After saving it will export the objects that are selected in a maya scene, if nothing is selected it exports the whole scene, and exports as an fbx file with a naming convention based on the environment.
Naming convention is "objectname_taskname_user_v###.ma" and "objectname_v###.fbx" and the files are saved into a maya folder and fbx folder respectively, inside an object folder in the environment directory.
'''
import os
import json
import maya.cmds as cmds
import maya.mel as mel

# Load FBX export settings from a JSON file
fbx_settings_file = "C:/Users/nicky/OneDrive/Documents/GitHub/Anim435Code/anim-435-2024-nj399/midterm/config/fbx.settings.json" # Update this path to your JSON file
try:
    with open(fbx_settings_file, 'r') as file:
        fbx_settings = json.load(file)
        print("FBX export settings loaded")
except Exception as e:
    print(f"Unable to load FBX export settings from JSON file: {e}")
    exit()

# Get environment variables
try:
    project_dir = os.getenv("PROJECT_DIR")
    object_name = os.getenv("OBJECT")
    task = os.getenv("TASK")
    user = os.getenv("USER")
except:
    print('Unable to access environment variables. Make sure you launched Maya using the gitbash command or similar')
    exit()

# Set the save location for the .ma file and ensure it exists
save_dir = f"{project_dir}/{object_name}/maya/"
if not os.path.exists(save_dir):
    try:
        os.makedirs(save_dir)
    except:
        print(f'Unable to create a folder in {save_dir}\nMake sure your directory and environment are set up correctly and in a space without admin permission')
        exit()

# Version number is based on the number of files in the maya folder
version_num = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]) + 1

# Create file name based on the object name and version number
file_name = f"{object_name}_{task}_{user}_v{version_num:03}"

cmds.file(rename=f'{save_dir}/{file_name}')
cmds.file(save=True, type='mayaAscii')

# Get the current selection in Maya
selection = cmds.ls(selection=True)

# Set the export location for the FBX file and ensure it exists
export_dir = f"{project_dir}/{object_name}/fbx/"
if not os.path.exists(export_dir):
    try:
        os.makedirs(export_dir)
    except:
        print(f'Unable to create a folder in {export_dir}\nMake sure your directory and environment are set up correctly and in a space without admin permission')
        exit()

# Apply FBX export settings from the JSON file
for setting, value in fbx_settings.items():
    # Convert the value to a string for MEL commands
    if isinstance(value, bool):
        value = 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        value = str(value)
    
    try:
        mel.eval(f'{setting} -v {value}')
    except Exception as e:
        print(f"Error applying FBX setting {setting}: {e}")

# Export the file with applied settings
mel.eval(f'FBXExport -f "{export_dir}{file_name}.fbx" -s')

# Print feedback to user to see where the files were saved
print(f'File saved: {save_dir}/{file_name}.ma')
print(f'File saved: {export_dir}{file_name}.fbx')
