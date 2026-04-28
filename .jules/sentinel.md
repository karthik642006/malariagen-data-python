## 2024-06-25 - [Arbitrary Code Execution in np.load]
**Vulnerability:** Use of `np.load` without `allow_pickle=False` could lead to arbitrary code execution if an attacker is able to construct a malicious `.npz` file in the cache directory.
**Learning:** `np.load` in older NumPy versions defaults to `allow_pickle=False` but can execute malicious pickled code if allowed or depending on version defaults. Even when loading from cache, untrusted input could be injected.
**Prevention:** Always explicitly set `allow_pickle=False` when using `np.load` to load cached array data, especially if the data's origin isn't strictly verified.
