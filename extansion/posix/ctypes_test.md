# Introduction

ctypes is a python built-in library that invokes exported functions from native compiled libraries.

## Common pitfalls

### Failing to load a file

``` python
>>> cdll.LoadLibrary("foobar.so")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/lib/python3.5/ctypes/__init__.py", line 425, in LoadLibrary
    return self._dlltype(name)
File "/usr/lib/python3.5/ctypes/__init__.py", line 347, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: foobar.so: cannot open shared object file: No such file or directory
```



ref. https://sodocumentation.net/python/topic/9050/ctypes
