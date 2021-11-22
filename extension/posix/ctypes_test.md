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
In this case, this is either because the file doesn't exists (or can't be found by the OS):

``` python
>>> cdll.LoadLibrary("libc.so")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/lib/python3.5/ctypes/__init__.py", line 425, in LoadLibrary
    return self._dlltype(name)
File "/usr/lib/python3.5/ctypes/__init__.py", line 347, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: /usr/lib/i386-linux-gnu/libc.so: invalid ELF header
```
In this case, 
 * the file is a script file and not a .so file.
 * This might also happen when trying to open a .dll file on a Linux machine
 * a 64bit file on a 32bit python interpreter.

### Failing to access a function

``` python
>>> libc.foo
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "/usr/lib/python3.5/ctypes/__init__.py", line 360, in __getattr__
    func = self.__getitem__(name)
File "/usr/lib/python3.5/ctypes/__init__.py", line 365, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: /lib/i386-linux-gnu/libc.so.6: undefined symbol: foo
```
In this case,
 * non-existing function is used.
 * should compile with g++ instead of gcc.(gcc does not link the binary with c++ libraries.)
 * should use C++ name mangling. (extern "C")
 * set library path like CMakeLists.txt using python env-path *LD_LIBRARY_PATH*

ref. https://sodocumentation.net/python/topic/9050/ctypes
