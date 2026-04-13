## 2024-05-24 - [CRITICAL] Prevent Insecure Deserialization in np.load
**Vulnerability:** Insecure deserialization via `np.load` allowing pickling.
**Learning:** Legacy `.npz` cache loading in `AnophelesBase.results_cache_get` utilized `np.load` without explicitly passing `allow_pickle=False`. This defaults or has historically defaulted to allowing execution of arbitrary code during deserialization, posing a severe risk if a cache path could be poisoned by a local attacker.
**Prevention:** Always pass `allow_pickle=False` when using `np.load()` on files that aren't 100% trusted, or universally as a defensive measure.
