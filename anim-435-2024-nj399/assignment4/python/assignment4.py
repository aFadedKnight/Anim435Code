'''
This script will save a maya file and name it based on the environment. After saving it will export the objects that are selected in a maya scene, if nothing is selected it exports the whole scene, and exports as an fbx file with a naming convention based on the environment.
Naming convention is "objectname_v###.ma" and "objectname_v###.fbx" and the files are saved into a maya folder and fbx folder respectively, inside an object folder in the environment directory.
'''
import os
import maya.cmds as cmds
import maya.mel as mel

#Get environment variables
try:
    proejct_dir = os.getenv("PROJECT_DIR")
    object_name= os.getenv("OBJECT")
except:
    print('Unable to access environment variables. Make sure you launced maya using the gitbash command or similar')
    exit()

#Set the save location for the .ma file and make sure it exists. Version number is based on the number of files in the maya folder
save_dir = f"{proejct_dir}/{object_name}/maya/"
if not os.path.exists(save_dir):
    try:
        os.makedirs(save_dir)
    except:
        print(f'Unable to create a folder in {save_dir}\nMake sure your directory and environment are setup correctlyand in a space without admin permission')
        exit()
version_num = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]) + 1

cmds.file(rename=f'{save_dir}/{object_name}_v{version_num:03}')
cmds.file(save=True, type='mayaAscii')

#Get the current selection in maya
selection = cmds.ls(selection=True)

#Set the export location for the fbx file and make sure it exists
export_dir = f"{proejct_dir}/{object_name}/fbx/"
if not os.path.exists(export_dir):
    try:
        os.makedirs(export_dir)
    except:
        print(f'Unable to create a folder in {export_dir}\nMake sure your directory and environment are setup correctly and in a space without admin permission')
        exit()

#Create file name based on the object name and version number
file_name = f"{object_name}_v{version_num:03}.fbx"

#Export the file with some predefined settings
mel.eval('FBXExportSmoothingGroups -v true')
mel.eval('FBXExportHardEdges -v false')
mel.eval(f'FBXExport -f "{export_dir}{file_name}" -s')

#Print feedback to user to see where the file was saved
print(f'File saved: {save_dir}/{object_name}_v{version_num:03}.ma')
print(f'File saved: {export_dir}{file_name}')