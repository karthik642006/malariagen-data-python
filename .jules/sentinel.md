
## 2024-05-20 - [CRITICAL] Fix Insecure Deserialization in NPZ Cache Loading
**Vulnerability:** Insecure deserialization via `np.load()` without explicitly setting `allow_pickle=False`. In `malariagen_data/anoph/base.py`, the `results_cache_get` method was loading legacy NPZ cache files dynamically using `np.load(legacy_results_path)`.
**Learning:** By default, `np.load()` in older versions of numpy or when unspecified can allow deserialization of arbitrary Python objects using `pickle`. Unauthenticated or manipulated cache files could exploit this to execute arbitrary code. The caching system inherently trusts the file contents on disk.
**Prevention:** Always explicitly set `allow_pickle=False` when using `np.load()` unless pickling is absolutely required. If it is required, consider using secure hashing/signatures to verify file integrity before loading, or migrate to safer serialization formats (like JSON or Parquet) depending on the data shape.
