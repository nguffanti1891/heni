import pandas as pd
import re

dim_df = pd.read_csv("heni/resources/dim_df_correct.csv")
result = []
for index, row in dim_df.iterrows():
    print(row['rawDim'].lower().replace("×","x"))
    dims = re.findall(r'(\d+(?:[,\,.]\d+)?)\s*x\s*(\d+(?:[,\,.]\d+)?)(?:\s*x\s*(\d+(?:[,\,.]\d+)?))?',row["rawDim"].lower().replace("×","x").replace("by","x"))
    result.append(dims[0])

#pe = dim_df.rawDim.str.extract(r'(\d{1,3}\s*[x,×]\s*\d{1,3}(?:\s*[x,×]\s*\d{1,3})?)')
#pe = dim_df.rawDim.str.extract(r'(\d+(?:[,\,.]\d+)?)\s*[x,×]\s*(\d+(?:[,\,.]\d+)?)(?:\s*[x,×]\s*(\d+(?:[,\,.]\d+)?))?')

#print(pe)


x = pd.DataFrame(result, columns=['height','width','depth'])
print(x)
#x.to_csv("output_task2.csv", index=False)