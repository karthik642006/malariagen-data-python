## 2024-05-31 - [High] Fix Pandas query string injection vulnerability
**Vulnerability:** Several places in the codebase use Python f-strings inside pandas dataframe `query()` methods (e.g., `df.query(f"col == '{val}'")`).
**Learning:** This introduces a code injection vulnerability, as an attacker controlling `val` could inject malicious code, especially given pandas default `engine='python'`.
**Prevention:** Always use safe parameter binding by replacing f-strings with standard boolean indexing (e.g., `df.loc[df["col"] == val]`) or `@` syntax (`df.query("col == @val")`).
