## 2026-05-17 - [Critical] Insecure Deserialization via np.load()
**Vulnerability:** Found `np.load()` being used without `allow_pickle=False` when loading cached results from `results.npz`.
**Learning:** Legacy cache files could be poisoned to execute arbitrary code when loaded by `np.load()` if pickling is enabled.
**Prevention:** Always explicitly use `allow_pickle=False` when calling `np.load()` on untrusted or cached files to ensure safe data deserialization without code execution risks.
