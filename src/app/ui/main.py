from pypdf import PdfReader
import pandas as pd
from pathlib import Path
import numpy as np

def generate_from_root(file: str) -> bool:

    path = Path(file)
    try:


        # Iterate through each path in the given path
        for x in path.iterdir():

            # If the given file is a directory, we can iterate through files
            if x.is_dir():

                # Set up the string fields
                columns_str = [
                    "Capstone_Group",
                    "advisor", 
                    "comments"
                ]

                # Set up the string dataframe
                df_str = pd.DataFrame(columns=columns_str)
                
                # Set up work for the number dataframe to fill columns dynamically
                col_num = []
                nums = []
                evals = []

                # Iterate through each file in the directory
                for prb in x.iterdir():
                    if (prb.suffix != ".pdf"): continue
                    # Data storage
                    data_num = dict()
                    data_str = dict()
                    
                    # Read the pdf and get their fillable fields
                    print(str(prb))
                    pdf = PdfReader(prb)
                    form_data = pdf.get_fields()

                    # Iterate through the fields to extract values
                    for field_name, field_value in form_data.items():                        
                        # Fill the string fields
                        if(columns_str.__contains__(field_name)):
                            data_str[field_name] = field_value.value

                        # Get evaluator
                        elif(field_name.__eq__('evaluator')):
                            eval = field_value.value
                            evals.append(eval)

                        # Fill the numerical fields
                        else:
                            try:
                                data_num[field_name] = float(field_value.value)

                            # If the value is N/A or just invalid, make it a NaN
                            # This allows it to exist but df.mean() will ignore
                            except ValueError:
                                data_num[field_name] = np.nan
                            except TypeError:
                                data_num[field_name] = np.nan
                            col_num.append(field_name)
                    
                    # Fill the DataFrames with the data
                    nums.append(data_num)
                    df_str.loc[eval,:] = data_str

                df_num = pd.DataFrame(nums, index=evals)
                # Create the average score from each evaluator
                df_num.loc["average", :] = df_num.mean()

                # Merge the DataFrames into one final DataFrame
                df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")

                # Create a file path for the excel file, and then convert the DataFrame into the excel file
                dir = x / "data.xlsx"
                df.to_excel(dir)


        # Indicate the program ran successfully 
        return True

    # In case of a bad path, don't crash the code, but give an error message
    except FileNotFoundError:
        print("The given path was invalid")
        return False
        
def generate_from_group(file: str) -> bool:

    path = Path(file)
    try:
        # If the given file is a directory, we can iterate through files
        if path.is_dir():

            # Set up the string fields
            columns_str = [
                "Capstone_Group",
                "advisor", 
                "comments"
            ]

            # Set up the string dataframe
            df_str = pd.DataFrame(columns=columns_str)

            # Set up work for the number dataframe to fill columns dynamically
            col_num = []
            nums = []
            evals = []

            # Iterate through each file in the directory
            for prb in path.iterdir():
                if (prb.suffix != ".pdf"): continue
                # Data storage
                data_num = dict()
                data_str = dict()
                
                # Read the pdf and get their fillable fields
                pdf = PdfReader(prb)
                form_data = pdf.get_fields()

                # Iterate through the fields to extract values
                for field_name, field_value in form_data.items():
                    # Fill the string fields
                    if(columns_str.__contains__(field_name)):
                        data_str[field_name] = field_value.value

                    # Get evaluator
                    elif(field_name.__eq__('evaluator')):
                        eval = field_value.value
                        evals.append(eval)

                    # Fill the numerical fields
                    else:
                        try:
                            data_num[field_name] = float(field_value.value)

                        # If the value is N/A or just invalid, make it a NaN
                        # This allows it to exist but df.mean() will ignore
                        except ValueError:
                            data_num[field_name] = np.nan
                        except TypeError:
                            data_num[field_name] = np.nan
                        col_num.append(field_name)
                    
                # Fill the DataFrames with the data
                nums.append(data_num)
                df_str.loc[eval,:] = data_str

            df_num = pd.DataFrame(nums, index=evals)
            # Create the average score from each evaluator
            df_num.loc["average", :] = df_num.mean()

            # Merge the DataFrames into one final DataFrame
            df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")

            # Create a file path for the excel file, and then convert the DataFrame into the excel file
            dir = path / "data.xlsx"
            df.to_excel(dir)

        # Indicate the program ran successfully 
        return True


    # In case of a bad path, don't crash the code, but give an error message
    except FileNotFoundError:
        print("The given path was invalid")

        # Indicate it broke
        return False
