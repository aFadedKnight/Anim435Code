import os, logging, json
import maya.cmds as cmds
import maya.mel as mel

logger = logging.getLogger(__name__)

FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s"

logging.basicConfig(filename='log.txt',level=logging.INFO, format=FORMAT)
logger.info('Starting')

# Load FBX export settings from a JSON file
fbx_settings_file = "C:/Users/nicky/OneDrive/Documents/GitHub/Anim435Code/anim-435-2024-nj399/midterm/config/fbx.settings.json"  # Update this path to your JSON file
try:
    logger.info(f'Loading fbx export settings from {fbx_settings_file}')
    with open(fbx_settings_file, 'r') as file:
        fbx_settings = json.load(file)
        print("FBX export settings loaded")
except Exception as e:
    logger.error(f"Unable to load FBX export settings from JSON file: {e}")
    exit()

# Get environment variables
try:
    logger.info('Loading project directory from environment')
    project_dir = os.getenv("PROJECT_DIR")
    logger.info('Loading object name from environment')
    object_name = os.getenv("OBJECT")
    logger.info('Loading task name from environment')
    task = os.getenv("TASK")
    logger.info('Loading username from environment')
    user = os.getenv("USER")

except Exception as e:
    logger.error(f'Unable to access environment variable. Make sure you launched Maya using the gitbash command or similar: {e}')
    exit()

# Set the save location for the .ma file and ensure it exists
logger.info('Checking for save directory')
save_dir = f"{project_dir}/{object_name}/maya/"
if not os.path.exists(save_dir):
    logger.warning(f"Save directory not found: {save_dir}")
    try:
        logger.info(f'Creating save directory: {save_dir}')
        os.makedirs(save_dir)
    except:
        logger.error(f'Unable to create a folder: {save_dir}\nMake sure your directory and environment are set up correctly and in a space without admin permission')
        exit()

logger.info('Accessing save directory to get version number')
# Version number is based on the number of files in the maya folder
version_num = len([f for f in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, f))]) + 1

logging.info('Creating file name')
# Create file name based on the object name and version number
file_name = f"{object_name}_{task}_{user}_v{version_num:03}"

logger.info(f'Renaming and saving maya file: {save_dir}/{file_name}.ma')
cmds.file(rename=f'{save_dir}/{file_name}')
cmds.file(save=True, type='mayaAscii')

logger.info('Getting maya selection')
# Get the current selection in Maya
selection = cmds.ls(selection=True)

logger.info('Checking for export directory')
# Set the export location for the FBX file and ensure it exists
export_dir = f"{project_dir}/{object_name}/fbx/"
if not os.path.exists(export_dir):
    logger.warning(f'Export directory not found: {export_dir}')
    try:
        logger.info(f'Creating export directory: {export_dir}')
        os.makedirs(export_dir)
    except:
        logger.error(f'Unable to create a folder: {export_dir}\nMake sure your directory and environment are set up correctly and in a space without admin permission')
        exit()

# Apply FBX export settings from the JSON file
logger.info('Applying fbx export settings')
for setting, value in fbx_settings.items():
    # Convert the value to a string for MEL commands
    if isinstance(value, bool):
        value = 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        value = str(value)
    
    # Execute each setting command separately
    mel_command = f'{setting} -v {value}'
    try:
        mel.eval(mel_command)
    except RuntimeError as e:
        logger.warning(f"Unable to apply fbx setting: {setting}: {e}")

# Export the file with applied settings
try:
    logger.info(f'Exporting fbx file: {export_dir}{file_name}.fbx')
    mel.eval(f'FBXExport -f "{export_dir}{file_name}.fbx" -s')
except RuntimeError as e:
    logger.error(f'Error exporting fbx file: {e}')

# Print feedback to user to see where the files were saved
logger.info(f'File saved: {save_dir}/{file_name}.ma')
logger.info(f'File saved: {export_dir}{file_name}.fbx')