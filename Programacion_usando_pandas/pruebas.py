from shutil import register_unpack_format
import pandas as pd
from datetime import datetime, timedelta

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
df_tbl0_c1_tbl2_c5b=pd.merge(tbl0[['_c0','_c1']],tbl2[['_c0','_c5b']])
tbl0_c1_tbl2_c5b_sum=df_tbl0_c1_tbl2_c5b.groupby('_c1')['_c5b'].sum()
print(tbl0_c1_tbl2_c5b_sum)