from pypdf import PdfReader
import pandas as pd

pdf = PdfReader("src/app/PRB1 Rubric (2).pdf")


# The function for all fields is get_fields() -> Return dict with field name as key

# form_data = pdf.get_form_text_fields()
form_data = pdf.get_fields()

for field_name, field_value in form_data.items():
    print(f"Field Name: {field_name}, Value: {field_value}")

# To access a specific field value:
specific_field_value = form_data.get("text_1ajch")
print(f"Value of 'Name_of_Your_Field': {specific_field_value}")

df = pd.DataFrame(
    columns=[
        "Capstone_Group",
        "Advisor", 
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
        ""
        ]
    )


# page = pdf.pages[0]

# text = page.extract_text()
# print(text)

# print(text[(text.index("Not at all Poor Neutral Good Outstanding")):])

