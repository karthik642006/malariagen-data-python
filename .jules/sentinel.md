
## 2024-05-18 - [CRITICAL] Code Injection via f-strings in pandas.DataFrame.query()
**Vulnerability:** Found multiple instances where `f"..."` strings were passed directly to `pandas.DataFrame.query()` (e.g. `df.query(f"ID == '{region}'")`).
**Learning:** This is particularly dangerous in this codebase because `.query()` is configured to default to `engine='python'` to support extension arrays. When an attacker provides a malicious value (like a region or inversion name) containing quotes and Python syntax, `eval` executes arbitrary Python code.
**Prevention:** Never use f-strings or `.format()` to construct query strings for pandas `.query()`. Always use `.loc[...]` with safe boolean indexing (e.g. `df.loc[df["ID"] == region]`) or pass variables safely into the query environment with `.query("ID == @region")` if `.query` is absolutely necessary.
