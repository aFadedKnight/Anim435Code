import maya.standalone
import maya.cmds as cmds
import argparse
import json, csv, os

maya.standalone.initialize(name="python")

def decimate(amount=50, file="", directory=""):
        """
        This function uses amount and will decimate geometry from a file based on the amount passed in.

        Args:
        amount = value to decimate gemoetry by
        file = name of the file that will be decimated
        directory = path to the file that will be decimated and where the new file will save

        Returns:
        None
        """
        print(amount,file,directory)

        # TO-DO: get information on original polycount

        # TO-DO: create code that will decimate geometry inside a given file.

        # Save File
        #maya.cmds.file(rename=r"new name in same directory")
        #maya.cmds.file(save=True)

        # Export CSV (needs variables in the data variable to be defined - geometry, og_polycount, new_polycount)
        '''
        csv_file = f'{directory}/{file}.{amount}.report.csv'

        data = [
            ['Geometry', 'OG Polycount', "New Polycount", "Amount Removed"],  # Headers
            [{geometry}, {og_polycount}, {new_polycount}, {amount}]
        ]
        
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        '''

 
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
    #if not os.path.exists(file_to_decimate):
    #    print('Path to file does not exist')
    #elif not file_to_decimate.endswith('.mb','.ma'):
    #     print('Path given was not a maya file')


    # Check if amount is an integer value if not get data from json
    try:
          amount = int(amount)
    except:
        lods = "C:\\Users\\nicky\\Documents\\GitHub\\Anim435Code\\anim-435-2024-nj399\\final\\config\\lods.json" # Change this to path of your json file
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