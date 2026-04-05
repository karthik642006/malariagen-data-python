## 2024-05-30 - Sentinel Journal
## 2024-05-30 - Fix Pandas Query Injection Risk
**Vulnerability:** User-supplied queries passed directly to `pandas.DataFrame.query()` or `eval()` can execute arbitrary Python code if `local_dict` and `global_dict` are not explicitly restricted.
**Learning:** Found an instance in `malariagen_data/anoph/phenotypes.py` where `sample_query` was evaluated without sandboxing, posing a Critical severity Remote Code Execution (RCE) risk.
**Prevention:** Always pop `local_dict` and `global_dict` from kwargs, and explicitly pass them as `{}` when calling pandas `.query()` or `.eval()`. Ensure `engine="python"` is used securely.
