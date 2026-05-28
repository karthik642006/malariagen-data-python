## 2024-05-18 - Pandas query() injection vulnerability
**Vulnerability:** Use of string interpolation (f-strings) inside `pandas.DataFrame.query()` expressions (e.g., `df.query(f"col == '{val}'")`).
**Learning:** This introduces severe code injection vulnerabilities because user-supplied strings can break out of the string context and execute arbitrary Python code, especially since `engine='python'` is frequently used in this codebase.
**Prevention:** Avoid string interpolation in `.query()`. Instead, use standard boolean indexing (e.g., `df.loc[df["col"] == val]`) or safe variable binding with `@` (e.g., `df.query("col == @val")`).
