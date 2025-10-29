import pandas as pd
import numpy as np
from pypdf import PDFReader

pdf = PDFReader(path_name)

form_data = pdf.get_fields()

df_num = pd.DataFrame()
df_str = pd.DataFrame()

columns_num=[
      "Project_Motivation", 
      "Constraints", 
      "Evaluation_Metrics", 
      "SotA", 
      "Design_Concepts", 
      "Concept_Selection", 
      "Budget", 
      "Schedule", 
      "Citations", 
      "Questions", 
      "Effective",
      ]
columns_str = [
    "Capstone_Group",
    "Advisor",
    "Comments"
]

df_num.loc[evaluators,columns_num] = form_data.for_num()

df_str.loc[evaluators, columns_str] = form_data.for_str()

df_num.loc["average", :] = df_num.mean()

df = df_num.merge(right=df_str, how='left', left_index=True, right_index=True).fillna("N/A")
