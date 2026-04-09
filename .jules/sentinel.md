## 2024-05-24 - Fix DataFrame query injection vulnerability
**Vulnerability:** Use of string interpolation (f-strings) inside `pandas.DataFrame.query()` expressions.
**Learning:** This repo frequently constructs queries like `df.query(f"ID == '{region}'")` using f-strings rather than using variable binding or direct indexing. This pattern is dangerous as it permits code injection into the pandas evaluation engine if user-supplied strings are interpolated.
**Prevention:** Always use safe variable binding (`df.query("ID == @region")`) or safer standard boolean indexing (`df.loc[df["ID"] == region]`) which avoids parsing strings entirely.
