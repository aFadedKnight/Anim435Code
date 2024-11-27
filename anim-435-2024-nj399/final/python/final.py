#import maya.standalone
#maya.standalone.initialize(name="python")
#import maya.cmds as cmds
import argparse
import json, csv

def decimate(amount=50, file=""):
        """
        This function uses amount and will decimate geometry from a file based on the amount passed in.

        Args:
        amount = value to decimate gemoetry by

        Returns:
        None
        """
        print(amount)
        print(file)
        # TO-DO: create code that will decimate geometry inside a given file.

        # Save File
        #maya.cmds.file(rename=r"new name in same directory")
        #maya.cmds.file(save=True)

        # Export CSV
        csv_file = f'{og_file_name}.{amount}.report.csv'

        data = [
            ['Geometry', 'OG Polycount', "New Polycount", "Amount Removed"],  # Headers
            [{geometry}, {og_polycount}, {new_polycount}, {amount}]
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

    amount="half"
    file_to_decimate="C:\\Users\\nicky\\Desktop"

    # Check if amount is an integer value if not get data from json
    try:
          amount = int(amount)
    except:
        lods = "..\\config\\lods.json"
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


    # Decimate File
    decimate(amount,file_to_decimate)

main()