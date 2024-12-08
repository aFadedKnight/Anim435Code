import maya.standalone
import maya.cmds as cmds
from datetime import datetime
import json, csv, os, argparse, logging

# Start mayapy
maya.standalone.initialize(name="python")

# Setting path to lods.json. This setting needs to be changed to your lods.json location
lods = "C:\\Users\\nicky\\Documents\\GitHub\\Anim435Code\\anim-435-2024-nj399\\final\\config\\lods.json" # Change this to path of your json file


#Setup Logger
logger = logging.getLogger(__name__)

FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s"

logging.basicConfig(filename='log.txt',level=logging.INFO, format=FORMAT)
logger.info('Starting')

def decimate(amount=50, file="", directory="", mode='preserve'):
        """
        This function uses amount and will decimate geometry from a file based on the amount passed in. 
        It will finish by saving out a new maya binary file with the decimated geometry and a csv file containing some metadata.

        Args:
        amount = value to decimate gemoetry by
        file = name of the file that will be decimated
        directory = path to the file that will be decimated and where the new file will save
        mode = determines settings to use for reducing geometry

        Returns:
        None
        """
        logger.info("Begin geometry reduction")
        # Open the Maya file
        maya_file = f'{directory}/{file}'
        cmds.file(maya_file, open=True, force=True)

        logger.info("Iterating through geo in file")
        logger.warning(f'Using {mode} mode to reduce geometry')
        # Iterate through geometry and reduce polycount
        all_meshes = cmds.ls(type="mesh")
        og_polycount = 0
        for mesh in all_meshes:
            og_polycount += cmds.polyEvaluate(mesh, face=True)
            if mode == 'preserve':
                cmds.polyReduce(mesh,p=amount,kqw=0.5,version=1)
            else: 
                cmds.polyReduce(mesh,p=amount)

        # Generate output filename
        output_file = (f"{maya_file}.{amount}.mb")

        # Save the decimated file
        cmds.file(rename=output_file)
        cmds.file(save=True, type="mayaBinary")
        logger.info(f"Decimated file saved as: {output_file}")

        logger.info('Generating CSV metadata')
        # Iterate through geometry and get polycount
        cmds.file(output_file, open=True, force=True)
        all_meshes = cmds.ls(type="mesh")
        new_polycount = 0
        for mesh in all_meshes:
            new_polycount += cmds.polyEvaluate(mesh, face=True)

        # Export csv file
        csv_file = f'{directory}/{file}.{amount}.report.csv'

        data = [
            ['File', 'OG Polycount', "New Polycount", "Percent Removed", "Log Date/Time"],  # Headers
            [file, og_polycount, new_polycount, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        ]
        
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            logger.warning(f"CSV file exported: {csv_file}")

 
def main():
    """
        This function sets up the argparse arguments and processes them to be passed through to the decimate() function

        Args:
        None

        Returns:
        None
        """
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Decimate geometry inside a file by a given amount")
    parser.add_argument('-a','--amount', type=str, default="half", help='Amount to decimate geometry. Can be string(half, quarter, two-thirds, third, eitgh, three-quarters) or specific integer value')
    parser.add_argument('-f','--file', type=str, help='Path to file that you want to decimate.')
    parser.add_argument('-m','--mode', type=str, help='Mode to decimate by, can be either the "decimate" which is more accurate to the amount you want to reduce geometry by but can mess up geo or the default "preserve" which preserves the geometry better but does not reduce as accurately.')

    args = parser.parse_args()
    amount = args.amount
    file_to_decimate = args.file
    mode =args.mode

    # Check file exists and is a maya file
    if not os.path.exists(file_to_decimate):
        logger.error(f"Path to file does not exsist: {file_to_decimate}")
        exit()
    elif not file_to_decimate.endswith('.ma') and not file_to_decimate.endswith('.mb'):
         logger.error(f"File given is not a maya file: {file_to_decimate}")
         exit()


    # Check if amount is an integer value if not get data from json
    try:
          logger.info("Chacking amount value")
          amount = int(amount)
    except:
        logger.info("Getting amount setting from lods.json")
        try:
            with open(lods, 'r') as file:
                lod_values = json.load(file)
            amount = amount.lower()
            try:
                 amount = lod_values[amount]
            except:
                 logger.error(f'Amount "{amount}" is not recognized')
                 exit()
            
        except Exception as e:
                logger.error(f"Unable to access lods.json file, can't load settings:\n{lods}\n{e}")
                exit()

    directory = os.path.dirname(file_to_decimate)
    file_to_decimate = os.path.basename(file_to_decimate)

    # Decimate File
    decimate(amount,file_to_decimate,directory, mode)

main()