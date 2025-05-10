# %%
import pandas as pd
import csv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler("log.log", mode='w+', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

def log_print(obj):
    if isinstance(obj, pd.DataFrame):
        logger.info(obj.to_string())
    else:
        logger.info(obj)

# %%
df = pd.read_csv("sub.txt", sep="\t", encoding="utf-8")

log_print("\n\nsub.txt head:")
log_print(df.head())

# %%
# count number of rows where null in sic

notNullDf = df[df["sic"].notnull()]
log_print("\n\nLength of Not null \"sic\" sub.txt")
log_print(len(notNullDf))

# %%
totalnData = len(df)
log_print("\n\nLength of sub.txt")
log_print(totalnData)

# %%
df_sic = pd.read_csv("data.txt", sep="\t", encoding="utf-8")
log_print("\n\nLength of \"sic\" sec.gov table")
log_print(df.head())

# %%
# log_print the unique sic codes in the sub.txt according to the data.txt

# distinct code in the sic sub.txt
codes = notNullDf["sic"]
sorted_codes = sorted(codes.unique().astype('int'))

log_print("\n\nSorted \"sic\" codes in sub.txt: ")
log_print(sorted_codes)

# %%
log_print("\n\nLength of sorted \"sic\" codes in sub.txt: ")
log_print(len(sorted_codes))

# %%
# count the number of companies in an industry sic code

sic_code_count_df = notNullDf["sic"].value_counts().reset_index()

log_print("\n\nHead for sic codes with counts for each")
log_print(sic_code_count_df.head())

# %%
unique_code_df = df_sic[df_sic["SIC Code"].isin(sorted_codes)]
unique_code_df = unique_code_df.rename(columns={'SIC Code': 'sic'})

log_print("\n\nHead for unique sic codes with industry and \"SIC Code\" renamed to \"sic\"")
log_print(unique_code_df.head())

# %%
merged_df = pd.merge(unique_code_df, sic_code_count_df, on="sic", how="inner")

filtered_df = merged_df[merged_df["sic"].isin(sorted_codes)]

log_print("\n\nMerged table and final output: ")
log_print(filtered_df[["Industry Title", "count"]])


# %%
log_print("\n\nTotal count for the \"count\" in the merged table: ")
log_print(filtered_df["count"].sum(axis=0))


