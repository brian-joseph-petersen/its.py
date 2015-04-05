Internet Time Service
---------------------
Python class for implementing [RFC 868 Time Protocol](http://tools.ietf.org/html/rfc868)

```python
import its

today = its.time()

today.strftime    # %Y-%m-%d %H:%M:%S
today.date        # %Y-%m-%d
today.time        # %H:%M:%S
today.year        # %Y
today.month       # %m
today.day         # %d
today.hour        # %H
today.minute      # %M
today.second      # %S
```