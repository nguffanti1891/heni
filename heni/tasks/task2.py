import pandas as pd
import re

dim_df = pd.read_csv("heni/resources/dim_df_correct.csv")
result = []
for index, row in dim_df.iterrows():
    if 'by' not in row["rawDim"]:
        dims = re.findall(r'(\d+(?:[,\,.]\d+)?)\s*x\s*(\d+(?:[,\,.]\d+)?)(?:\s*x\s*(\d+(?:[,\,.]\d+)?))?\s*[cm]\s*',row["rawDim"].lower().replace("×","x").replace("by","x"))
        result.append(dims[len(dims)-1])
    else:
        dims = re.findall(r'(\d+(?:[,\,.]\d+)?)\s*by\s*(\d+(?:[,\,.]\d+)?)(?:\s*by\s*(\d+(?:[,\,.]\d+)?))?',row["rawDim"].lower())
        result.append((float(dims[0][0])*2.54,float(dims[0][1])*2.54,''))

x = pd.DataFrame(result, columns=['height','width','depth'])
x.to_csv("output_task2.csv", index=False)