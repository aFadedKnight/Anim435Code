import maya.standalone
maya.standalone.initialize(name="python")
import maya.cmds as cmds
import argparse


def make_building(num_floors=1):
        """
        This function creates a building with a given number of floors.
        """

        print("Creating building")

        numFloors = num_floors
        
        # Defining height of building, roof, and door placement
        baseHeight = numFloors * 5
        roofHeight = (baseHeight/2) + 1.765
        doorHeight = -(baseHeight/2) + 1

        # Create Building Geometry
        buildingCube = cmds.polyCube(height=baseHeight, depth=5, width=5, name='buildingBody')
        buildingRoof = cmds.polyPyramid(sideLength=5, name='buildingRoof')
        buildingDoor = cmds.polyCube(height=2, depth=0.5, width=1.25, name='buildingDoor')

        # Positioning Building geometry and grouping
        cmds.move(0, roofHeight, 0, buildingRoof)
        cmds.move(0, doorHeight, 2.5, buildingDoor)
        cmds.rotate(0, '45deg', 0, buildingRoof)
        cmds.group(buildingCube, buildingRoof, buildingDoor, name='Building_0')

def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description="Create a building in Maya with a given number of floors.")
    parser.add_argument('--floors', type=int, default=1, help='Number of floors for the building')

    args = parser.parse_args()
    num_floors = args.floors

    # Create the building
    make_building(num_floors)

    maya.cmds.file(rename=r"C:\Users\nicky\OneDrive\Documents\GitHub\Anim435Code\anim-435-2024-nj399\assignment3\bin\newbuilding.mb")
    maya.cmds.file(save=True)

    print(f"Building with {num_floors} floors created.")

main()
