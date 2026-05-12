## 2024-05-18 - [Insecure Deserialization in Caching]
**Vulnerability:** Found `np.load()` reading cached NPZ files without explicitly disabling pickling (`allow_pickle=False`).
**Learning:** Legacy cache loading processes can become code injection vectors. The default behavior of `np.load()` in older Numpy versions or unspecified contexts allows the unpickling of arbitrary Python objects, which could lead to remote code execution if cache files are tampered with.
**Prevention:** Always explicitly set `allow_pickle=False` when using `np.load()` to read files, especially when loading data from a file system that could potentially be modified by untrusted actors.
