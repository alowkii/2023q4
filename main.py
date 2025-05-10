# %%
import pandas as pd
import csv

# %%
df = pd.read_csv("sub.txt", sep="\t", encoding="utf-8")

print(df.head())

# %%
# count number of rows where null in sic

notNullDf = df[df["sic"].notnull()]
print(len(notNullDf))

# %%
totalnData = len(df)
print(totalnData)

# %%
df_sic = pd.read_csv("data.txt", sep="\t", encoding="utf-8")
print(df)

# %%
# print the unique sic codes in the sub.txt according to the data.txt

# distinct code in the sic sub.txt
codes = notNullDf["sic"]
sorted_codes = sorted(codes.unique().astype('int'))

print(sorted_codes)

# %%

print(len(sorted_codes))

# %%
# count the number of companies in an industry sic code

sic_code_count_df = notNullDf["sic"].value_counts().reset_index()

print(sic_code_count_df)

# %%
unique_code_df = df_sic[df_sic["SIC Code"].isin(sorted_codes)]
unique_code_df = unique_code_df.rename(columns={'SIC Code': 'sic'})

print(unique_code_df)

# %%
merged_df = pd.merge(unique_code_df, sic_code_count_df, on="sic", how="inner")

filtered_df = merged_df[merged_df["sic"].isin(sorted_codes)]

print(filtered_df[["Industry Title", "count"]])


# %%
filtered_df["count"].sum(axis=0)
