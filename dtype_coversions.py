Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=9
>>> print(a)
9
>>> int(8)
8
>>> int(7.0)
7
>>> int('hi')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('hi')
ValueError: invalid literal for int() with base 10: 'hi'
>>> int(3+3j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+3j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> float(4)
4.0
>>> float('hi')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float('hi')
ValueError: could not convert string to float: 'hi'
float(2+4j)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(2+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(7282)
'7282'
str(73.86)
'73.86'
str(3+5j)
'(3+5j)'
str(True)
'True'
str(False)
'False'
complex(3)
(3+0j)
complex(3+4j)
(3+4j)
complex(73.86)
(73.86+0j)
complex('hi')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    complex('hi')
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
bool('hi')
True
bool(2)
True
bool(2+4j)
True
bool(3.1)
True
bool(True)
True
bool(False)
False
