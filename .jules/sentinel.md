## 2024-05-24 - [Fix np.load arbitrary code execution]
**Vulnerability:** `np.load()` was used without `allow_pickle=False` when loading legacy `.npz` files from the results cache.
**Learning:** Cached data (even local) should be treated as potentially untrusted if it can lead to code execution. The transition to Zarr helps, but backwards compatibility code paths using `np.load` still carry risk.
**Prevention:** Always explicitly use `allow_pickle=False` with `np.load()`, or use safer serialization formats like Zarr or HDF5.
