## 2024-05-30 - Fix pandas query injection vulnerabilities
**Vulnerability:** String interpolation (f-strings) used inside `pandas.DataFrame.query()` expressions (e.g., `df.query(f"ID == '{region}'")`). With `engine='python'` (which is default/explicitly set in this project), this allows arbitrary Python code execution if user input like `region` is malicious.
**Learning:** Pandas `.query()` evaluates expressions dynamically. Interpolating untrusted strings directly into query expressions allows breaking out of the string literal and injecting arbitrary evaluation logic.
**Prevention:** Use pandas boolean indexing (e.g., `df.loc[df['ID'] == region]`) instead of dynamically constructed query strings, or use safe variable binding (`@var`) when `.query()` is strictly necessary.
