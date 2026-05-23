## 2024-06-11 - Arbitrary Code Execution in numpy.load
**Vulnerability:** Arbitrary code execution vulnerability due to calling `numpy.load()` without `allow_pickle=False` when reading potentially untrusted cached NPZ files (`malariagen_data/anoph/base.py`).
**Learning:** Legacy caching mechanisms using `np.load` on numpy `.npz` files default to `allow_pickle=True` in older numpy versions, or if enabled, allowing arbitrary code execution if an attacker modifies or supplies a compromised cache file.
**Prevention:** Always explicitly set `allow_pickle=False` when using `numpy.load` unless pickling is strictly required and the input is guaranteed to be trusted.
