import pandas as pd
import re

dim_df = pd.read_csv("heni/resources/dim_df_correct.csv")
result = []
for index, row in dim_df.iterrows():
    print(row['rawDim'].lower().replace("×","x"))
    dims = re.findall(r'(\d+(?:[,\,.]\d+)?)\s*x\s*(\d+(?:[,\,.]\d+)?)(?:\s*x\s*(\d+(?:[,\,.]\d+)?))?',row["rawDim"].lower().replace("×","x").replace("by","x"))
    result.append(dims[0])

x = pd.DataFrame(result, columns=['height','width','depth'])
x.to_csv("output_task2.csv", index=False)