# http-cache

An HTTP client wrapper with ETag support and an on-disk response cache.

## Why

The existing libraries were either abandoned or pulled in a large dependency tree.

## Install

```bash
pip install http-cache
```

## Usage

```python
from http_cache import httpCache

result = httpCache("example")
print(result)
```

## Notes

- No runtime dependencies outside the standard library.
- Tested on Python 3.9 and newer.

## License

MIT
