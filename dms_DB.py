
import pandas as pd

# data path
data_path = "./data/DMS_DB.xlsx"


def get_similar_crisis_list (sector):

    # Read the Excel file
    df = pd.read_excel(data_path, engine='openpyxl')
    # get crisis list in this sector
    results = df.loc[df["Sector"] == sector]
    crisis_list = list(set(results["Crisis"]))
    
    return crisis_list


def get_action (crisis, sector):
        
        # Read the Excel file
        df = pd.read_excel(data_path, engine='openpyxl')

        # Filter the dataFrame for rows with the specified crisis and sector
        subset_df = df[(df["Crisis"] == crisis) & (df["Sector"] == sector)]

        # Extract the Action and Evaluation columns and pair them
        action = list(zip(subset_df["Action"]))

        if len(action) > 0: action = action[0][0]
        else: action = None

        return action
