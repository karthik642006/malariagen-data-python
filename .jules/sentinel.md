## 2024-05-18 - Prevent Code Injection in Pandas Query
**Vulnerability:** Code injection vulnerability existed due to the use of string interpolation (f-strings) inside `pandas.DataFrame.query()` and `eval()` expressions (e.g., `df.query(f"ID == '{region}'")`). Because pandas uses `engine='python'`, this allowed arbitrary code execution.
**Learning:** Always use safe variable binding (`@` syntax) instead of string interpolation for pandas queries when working with user inputs.
**Prevention:** Use standard boolean indexing or safe variable binding via `@` in `query` and `eval` expressions.
