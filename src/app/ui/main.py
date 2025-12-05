from pypdf import PdfReader
import pandas as pd
from pathlib import Path
import numpy as np

def generate_from_root(file):

    path = Path(file)
    try:
        # Iterate through each path in the given path
        for x in path.iterdir():

            # If the given file is a directory, we can iterate through files
            if x.is_dir():

                # Set up the pandas DataFrames
                columns_num=[
                    "project_motivation", 
                    "constraints", 
                    "evaluation_metrics", 
                    "state_of_the_art", 
                    "design_concepts", 
                    "concept_selection", 
                    "budget", 
                    "schedule", 
                    "citations", 
                    "questions", 
                    "effective",
                ]        
                columns_str = [
                    "Capstone_Group",
                    "advisor", 
                    "comments"
                ]
                df_num = pd.DataFrame(columns=columns_num)
                df_str = pd.DataFrame(columns=columns_str)

                # Iterate through each file in the directory
                for prb in x.iterdir():
                    # Data storage
                    data_num = dict()
                    data_str = dict()
                    
                    # Read the pdf and get their fillable fields
                    pdf = PdfReader(prb)
                    form_data = pdf.get_fields()

                    # Iterate through the fields to extract values
                    for field_name, field_value in form_data.items():
                        # Fill the numerical fields
                        if(columns_num.__contains__(field_name)) :
                            try:
                                data_num[field_name] = float(field_value.value)
                            except ValueError:
                                data_num[field_name] = 0
                        
                        # Fill the string fields
                        if(columns_str.__contains__(field_name)):
                            data_str[field_name] = field_value.value

                        # Get evaluator
                        if(field_name.__eq__('evaluator')):
                            eval = field_value.value
                    
                    # Fill the DataFrames with the data
                    df_num.loc[eval,:] = data_num
                    df_str.loc[eval,:] = data_str

                # Create the average score from each evaluator
                df_num.loc["average", :] = df_num.mean()

                # Merge the DataFrames into one final DataFrame
                df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")

                # Create a file path for the excel file, and then convert the DataFrame into the excel file
                dir = x / "data.xlsx"
                df.to_excel(dir)

    # In case of a bad path, don't crash the code, but give an error message
    except FileNotFoundError:
        print("The given path was invalid")
        
def generate_from_root(file):

    path = Path(file)
    try:
        # If the given file is a directory, we can iterate through files
        if path.is_dir():

            # Set up the pandas DataFrames
            columns_num=[
                "project_motivation", 
                "constraints", 
                "evaluation_metrics", 
                "state_of_the_art", 
                "design_concepts", 
                "concept_selection", 
                "budget", 
                "schedule", 
                "citations", 
                "questions", 
                "effective",
            ]        
            columns_str = [
                "Capstone_Group",
                "advisor", 
                "comments"
            ]
            df_num = pd.DataFrame(columns=columns_num)
            df_str = pd.DataFrame(columns=columns_str)

            # Iterate through each file in the directory
            for prb in x.iterdir():
                # Data storage
                data_num = dict()
                data_str = dict()
                
                # Read the pdf and get their fillable fields
                pdf = PdfReader(prb)
                form_data = pdf.get_fields()

                # Iterate through the fields to extract values
                for field_name, field_value in form_data.items():
                    # Fill the numerical fields
                    if(columns_num.__contains__(field_name)) :
                        try:
                            data_num[field_name] = int(field_value.value)
                        except ValueError:
                            data_num[field_name] = 0
                    
                    # Fill the string fields
                    if(columns_str.__contains__(field_name)):
                        data_str[field_name] = field_value.value

                    # Get evaluator
                    if(field_name.__eq__('evaluator')):
                        eval = field_value.value
                
                # Fill the DataFrames with the data
                df_num.loc[eval,:] = data_num
                df_str.loc[eval,:] = data_str

            # Create the average score from each evaluator
            df_num.loc["average", :] = df_num.mean()

            # Merge the DataFrames into one final DataFrame
            df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")

            # Create a file path for the excel file, and then convert the DataFrame into the excel file
            dir = path / "data.xlsx"
            df.to_excel(dir)

    # In case of a bad path, don't crash the code, but give an error message
    except FileNotFoundError:
        print("The given path was invalid")
