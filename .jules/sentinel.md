## 2023-10-26 - [CRITICAL] Pandas Query Code Injection
**Vulnerability:** Arbitrary code execution via `pandas.DataFrame.query` using f-strings for user input.
**Learning:** The codebase defaults to using `engine='python'` in pandas evaluations to support extension array dtypes. Because of this, standard f-string interpolation inside `.query()` calls becomes a critical code injection vector if the input is untrusted.
**Prevention:** Never use string interpolation (f-strings) inside `pandas.DataFrame.query()`. Always use standard boolean indexing (e.g., `df.loc[df["col"] == val]`) or safe variable binding (`df.query("col == @val")`).
