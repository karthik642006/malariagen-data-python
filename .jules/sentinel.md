## 2024-05-18 - Pandas Query Injection
**Vulnerability:** Found `pandas.DataFrame.query()` calls using f-strings for user inputs (e.g., `gene_annotation.query(f"ID == '{region}'")`).
**Learning:** `pandas.DataFrame.query(..., engine="python")` executes an underlying `eval()` using the `engine="python"`. Because f-strings interpolate the value into the query string before parsing, this allows arbitrary code execution via syntax injection if the user input is not sanitized or escapes the string literal.
**Prevention:** Avoid f-strings inside `query()`. Use boolean indexing (`df.loc[df["col"] == val]`) or `@variable` binding (`df.query("col == @val")`) for external data.
