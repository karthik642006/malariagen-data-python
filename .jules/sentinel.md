## 2024-05-24 - Pandas Query Injection via f-strings
**Vulnerability:** Critical code injection vulnerability in pandas `DataFrame.query()` expressions. f-strings were being used to construct queries with unsanitized user input (e.g., `df.query(f"ID == '{region}'")`).
**Learning:** Because the codebase uses `engine='python'` in pandas evaluations to support extension array dtypes, constructed query strings are executed dynamically. Injecting values via f-strings enables arbitrary Python code execution if input contains malicious payload like `' or @__import__('os').system('...') == '`.
**Prevention:** Always use safe variable binding syntax (e.g., `df.query("ID == @region")`) or boolean masking (e.g., `df.loc[df["ID"] == region]`) instead of string interpolation for pandas queries.
