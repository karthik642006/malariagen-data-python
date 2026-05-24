## 2024-05-24 - [Pandas Query Code Injection]
**Vulnerability:** Pandas `query()` calls using f-strings with variables (e.g. `df.query(f"ID == '{region}'")`) allow for arbitrary code execution because `engine='python'` is frequently used in pandas evaluation.
**Learning:** Python evaluates f-strings before passing the query string to pandas. If the string contains user input, the input can alter the query structure or inject malicious python code.
**Prevention:** Use pandas parameter binding via the `@` symbol (e.g., `df.query("ID == @region")`) or standard boolean indexing (`df[df["ID"] == region]`) which safely bounds variables into the query environment.
