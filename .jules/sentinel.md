## 2024-05-15 - [CRITICAL] Arbitrary code execution vulnerability in np.load()
**Vulnerability:** Found `np.load(legacy_results_path)` without `allow_pickle=False` in `malariagen_data/anoph/base.py`.
**Learning:** `np.load()` is vulnerable to arbitrary code execution if a maliciously crafted `.npz` file is provided, because it can deserialize arbitrary Python objects if `allow_pickle=True`. The default has changed in recent numpy versions, but it's best practice to explicitly state `allow_pickle=False` to ensure security regardless of numpy version.
**Prevention:** Always use `np.load(..., allow_pickle=False)` when loading untrusted or cached `.npy`/`.npz` files unless pickling is explicitly required and the source is trusted.
