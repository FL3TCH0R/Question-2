Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def loop():
...     for i in range(0, 6):
...         num=1
...         for j in range(0, i+1):
...             print(num, end=" ")
...             num=num+1
... 
...             
>>> loop()
1 1 2 1 2 3 1 2 3 4 1 2 3 4 5 1 2 3 4 5 6 
