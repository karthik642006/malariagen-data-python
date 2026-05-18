## 2024-05-24 - [Fix pandas query injection vulnerabilities]
**Vulnerability:** Pandas `query()` or `eval()` using f-strings with user-controlled input (e.g., `query(f"ID == '{region}'")`). This allowed arbitrary code execution.
**Learning:** Pandas query syntax with `engine='python'` executes code and is highly susceptible to injection if f-strings are used.
**Prevention:** Use pandas parameter binding via the `@` symbol (e.g., `query("ID == @region")`) to safely pass variables without risk of code injection.