## 2024-05-24 - Explicitly disable pickle in np.load
**Vulnerability:** Arbitrary Code Execution (Insecure Deserialization)
**Learning:** `np.load()` was used without explicitly setting `allow_pickle=False` when loading legacy cache files, potentially allowing arbitrary code execution if a cache file is tampered with or untrusted data is processed.
**Prevention:** Always explicitly pass `allow_pickle=False` to `np.load()`, especially when loading cached data.
