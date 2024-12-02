import maya.standalone
import maya.cmds as cmds
import argparse
import json, csv, os

maya.standalone.initialize(name="python")

def decimate(amount=50, file="", directory=""):
        """
        This function uses amount and will decimate geometry from a file based on the amount passed in. 
        It will finish by saving out a new maya binary file with the decimated geometry and a csv file containing some metadata.

        Args:
        amount = value to decimate gemoetry by
        file = name of the file that will be decimated
        directory = path to the file that will be decimated and where the new file will save

        Returns:
        None
        """
        # Open the Maya file
        maya_file = f'{directory}/{file}'
        cmds.file(maya_file, open=True, force=True)

        # Iterate through geometry and reduce polycount
        all_meshes = cmds.ls(type="mesh")
        og_polycount = 0
        for mesh in all_meshes:
            og_polycount += cmds.polyEvaluate(mesh, face=True)
            cmds.polyReduce(mesh,p=amount,kqw=0.5, version=1)

        # Generate output filename
        output_file = (f"{maya_file}.{amount}.mb")

        # Save the decimated file
        cmds.file(rename=output_file)
        cmds.file(save=True, type="mayaBinary")
        print(f"Decimated file saved as: {output_file}")

        # Iterate through geometry and get polycount
        cmds.file(output_file, open=True, force=True)
        all_meshes = cmds.ls(type="mesh")
        new_polycount = 0
        for mesh in all_meshes:
            new_polycount += cmds.polyEvaluate(mesh, face=True)

        # Export csv file
        csv_file = f'{directory}/{file}.{amount}.report.csv'

        data = [
            ['File', 'OG Polycount', "New Polycount", "Percent Removed"],  # Headers
            [file, og_polycount, new_polycount, amount]
        ]
        
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

 
def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Decimate geometry inside a file by a given amount")
    parser.add_argument('-a','--amount', type=str, default="half", help='Amount to decimate geometry. Can be string(half, quarter, two-thirds, third, eitgh, three-quarters) or specific integer value')
    parser.add_argument('-f','--file', type=str, help='Path to file that you want to decimate.')

    args = parser.parse_args()
    amount = args.amount
    file_to_decimate = args.file

    #amount="half"
    #file_to_decimate="C:/Projects/file.ma"

    # Check file exists and is a maya file
    if not os.path.exists(file_to_decimate):
        print('Path to file does not exist')
    elif not file_to_decimate.endswith('.ma') and not file_to_decimate.endswith('.mb'):
         print('Path given was not a maya file')


    # Check if amount is an integer value if not get data from json
    try:
          amount = int(amount)
    except:
        lods = "C:\\Users\\nicky\\OneDrive\\Documents\\GitHub\\Anim435Code\\anim-435-2024-nj399\\final\\config\\lods.json" # Change this to path of your json file
        try:
            with open(lods, 'r') as file:
                lod_values = json.load(file)
            amount = amount.lower()
            try:
                 amount = lod_values[amount]
            except:
                 print(f'Amount "{amount}" not recognized')
                 exit()
            
        except Exception as e:
                print("Unable to open JSON file")
                exit()

    directory = os.path.dirname(file_to_decimate)
    file_to_decimate = os.path.basename(file_to_decimate)

    print(directory)

    # Decimate File
    decimate(amount,file_to_decimate,directory)

main()