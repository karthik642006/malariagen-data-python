## 2024-05-30 - Fix code injection vulnerability in pandas query evaluation
**Vulnerability:** Unrestricted use of `pandas.DataFrame.eval()` and `pandas.DataFrame.query()` with user-provided strings without securing the `local_dict` and `global_dict`. This exposes an attacker to run arbitrary code using Python's `__builtins__`.
**Learning:** `pandas.eval` and `pandas.query` evaluate expressions in the local and global context by default. This makes user-supplied `query` strings a vector for code injection vulnerabilities (RCE).
**Prevention:** Always restrict evaluation scopes when passing uncontrolled input to `pandas.query` or `pandas.eval` by explicitly assigning `local_dict={}` and `global_dict={}`.
