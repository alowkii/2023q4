# %%
import pandas as pd
import csv

# %%
df = pd.read_csv("sub.txt", sep="\t", encoding="utf-8")

print(df.head())

# %%
#count number of rows where null in sic

notNullDf = df[df["sic"].notnull()]
print(len(notNullDf))

# %%
totalNoData = len(df)
print(totalNoData)

# %%
df_sic = pd.read_csv("data.txt", sep="\t", encoding="utf-8")
print(df)

# %%
#print the unique sic codes in the sub.txt according to the data.txt

#distinct code in the sic sub.txt
codes = notNullDf["sic"]
sorted_codes = sorted(codes.unique().astype('int'))

print(sorted_codes)

# %%

print(len(sorted_codes))

# %%
matching_codes = []
for x in sorted_codes:
    for a in df_sic.iterrows():
        if x == a[1].iloc[0]:
            matching_codes.append(a[1])

# %%
print("Count of matching codes", len(matching_codes))
print(matching_codes)


