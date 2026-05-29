## 2024-05-15 - [Insecure Deserialization via np.load]
**Vulnerability:** Found `np.load(legacy_results_path)` without `allow_pickle=False`.
**Learning:** `numpy.load` with `allow_pickle=True` (which used to be default in older numpy and can be a risk) allows arbitrary code execution if a maliciously crafted `.npz` or `.npy` file is loaded. Even if it's cached data, it's safer to explicitly disable pickle.
**Prevention:** Always use `allow_pickle=False` when using `np.load` on untrusted or potentially compromised files, and default to it for safety.
