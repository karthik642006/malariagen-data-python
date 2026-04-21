## 2025-03-08 - Fix arbitrary code execution in `numpy.load`
**Vulnerability:** `np.load()` was called without `allow_pickle=False` in `malariagen_data/anoph/base.py`, allowing for potential arbitrary code execution if a maliciously crafted `.npz` file was cached and loaded.
**Learning:** `np.load()` defaults to `allow_pickle=False` only in newer numpy versions (>=1.16.3). In this project, `numpy.load()` was used for legacy backwards compatibility `.npz` files and without explicit protection, making it a critical security vulnerability for any system relying on the cache.
**Prevention:** Always use `allow_pickle=False` explicitly when calling `np.load()` with untrusted or locally-cached files unless you fully control the content and expect pickled objects.
