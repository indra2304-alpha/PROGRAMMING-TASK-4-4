Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from textwrap import wrap
... def merge_the_tools(string, k):
...     ls = wrap(string, k)
...     new_ls = []
...     for x in ls:
...         result = x[0]
...         for i in range(1,len(x)):
...             if x[i] not in result:
...                 result += x[i]
...             else: 
...                 continue
...         print(result)
... if __name__ == '__main__':
...     string, k = input(), int(input())
