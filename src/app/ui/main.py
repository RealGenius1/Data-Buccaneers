from pypdf import PdfReader
import pandas as pd
from pathlib import Path
import numpy as np

def generate(file, dest):

    path = Path(file)
    for x in path.iterdir():
        if x.is_dir():
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

            for prb in x.iterdir():
                data_num = dict()
                data_str = dict()
                
                pdf = PdfReader(prb)
                form_data = pdf.get_fields()
                for field_name, field_value in form_data.items():
                    if(columns_num.__contains__(field_name)) :
                        try:
                            data_num[field_name] = int(field_value.value)
                        except ValueError:
                            data_num[field_name] = 0
                    if(columns_str.__contains__(field_name)):
                        data_str[field_name] = field_value.value
                    if(field_name.__eq__('evaluator')):
                        eval = field_value.value
                
                df_num.loc[eval,:] = data_num
                df_str.loc[eval,:] = data_str

            df_num.loc["average", :] = df_num.mean()
            df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")

            dir = x / "data.xlsx"
            df.to_excel(dir)