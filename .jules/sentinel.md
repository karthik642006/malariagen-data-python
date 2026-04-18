## 2025-02-14 - Fix Insecure Deserialization in np.load
**Vulnerability:** Arbitrary code execution vulnerability via insecure deserialization. `np.load` in `malariagen_data/anoph/base.py` was used without explicitly specifying `allow_pickle=False` when loading cached array data.
**Learning:** Even internal cache loading needs to be defended against insecure deserialization, as attackers could potentially modify cache files locally or if the cache is populated from an external/shared source.
**Prevention:** Always explicitly set `allow_pickle=False` when using `np.load` unless pickling is strictly required (in which case, the data source must be fully trusted and authenticated).
