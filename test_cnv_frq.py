import pandas as pd
df = pd.DataFrame({'type': ['a', 'b', 'c']})
q = "a"
# What about cnv_frq.py f-string?
print(df.loc[df['type'] == q])
