
import numpy as np
import pandas as pd
df = pd.read_csv("amazon_cells_labelled.tsv",
        sep="\t",
        header=None,
        names=['msg','lbl']
    )
df_tagged_1 = df.dropna()
df_tagged_2 = df[(df["lbl"] >= 0)]
df_tagged = df[df["lbl"].notnull()]
print(df_tagged==df_tagged_1)
