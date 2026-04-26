## 2024-05-24 - [Insecure Deserialization in np.load]
**Vulnerability:** Found `np.load()` usage without `allow_pickle=False` when loading legacy NPZ cache files. This could allow arbitrary code execution if an attacker modifies the cache file.
**Learning:** `numpy.load` historically defaulted to `allow_pickle=True` (changed in later versions but best to be explicit). When loading cached data files (which might be shared or manipulated), insecure deserialization can lead to RCE.
**Prevention:** Always explicitly set `allow_pickle=False` when using `np.load()`, especially on files that might be from an untrusted source or manipulated locally.
