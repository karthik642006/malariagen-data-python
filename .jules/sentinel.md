## 2024-05-24 - Insecure Deserialization in Caching
**Vulnerability:** `np.load()` was used without `allow_pickle=False` in cache loading logic (`malariagen_data/anoph/base.py`).
**Learning:** By default, older versions of numpy or certain usages of `np.load` can allow unpickling of Python objects, leading to arbitrary code execution if a local cache is poisoned.
**Prevention:** Always explicitly use `allow_pickle=False` when loading `.npz` or `.npy` files unless picking is absolutely required and the file source is fully trusted.
