Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data types in python
>>> a=10
>>> type(a)
<class 'int'>
>>> b=3.5
>>> type(b)
<class 'float'>
>>> c="python"
>>> type(c)
<class 'str'>
>>> x='python'
>>> type(x)
<class 'str'>
>>> y='''hello'''
>>> type(y)
<class 'str'>
>>> a+8i
SyntaxError: invalid decimal literal
>>> type(a+9j)
<class 'complex'>
>>> T=true
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    T=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> T=True
>>> type(T)
<class 'bool'>
