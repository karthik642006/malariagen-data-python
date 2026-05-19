## 2024-05-15 - Fix insecure deserialization in `AnophelesBase.results_cache_get`
**Vulnerability:** `np.load()` was called without `allow_pickle=False` when loading cached results from `results.npz` files.
**Learning:** `np.load()` defaults to `allow_pickle=False` in recent numpy versions, but it's best practice to explicitly enforce it for safety, especially if older numpy versions are used or it's implicitly allowed. An attacker could exploit this by modifying cached `results.npz` files, leading to arbitrary code execution when loaded.
**Prevention:** Always explicitly set `allow_pickle=False` when calling `np.load()` with untrusted data or cached files.
