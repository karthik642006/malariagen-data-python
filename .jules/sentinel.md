## 2024-05-24 - [Fix np.load Remote Code Execution Vulnerability]
**Vulnerability:** Arbitrary code execution vulnerability via insecure `np.load` usage without `allow_pickle=False`.
**Learning:** Legacy results caching code in `AnophelesBase.results_cache_get` read `.npz` files using default `np.load` parameters, which can allow arbitrary Python code execution if a maliciously crafted numpy array file is loaded.
**Prevention:** Always explicitly specify `allow_pickle=False` when using `np.load()` to prevent arbitrary code execution, especially for files that might be influenced or modified by users or untrusted sources.
