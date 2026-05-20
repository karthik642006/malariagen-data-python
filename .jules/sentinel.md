## 2024-05-23 - Insecure Deserialization in np.load
**Vulnerability:** Insecure deserialization of untrusted data in `np.load` without explicitly setting `allow_pickle=False`.
**Learning:** Legacy caching mechanisms using `.npz` files rely on `numpy.load()`. By default in older numpy versions, or if implicitly assumed safe, this could allow arbitrary code execution via object deserialization if the cached `.npz` file is compromised or tampered with by a malicious actor.
**Prevention:** Always explicitly set `allow_pickle=False` when using `numpy.load()` to prevent arbitrary code execution vulnerabilities from untrusted files, especially when loading cached data.
