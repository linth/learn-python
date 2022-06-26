# Tips for better python performance

## Timeit
```python
def test_func():
  # the code to be tested
    arr = []
    for i in range(500):
        arr.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_func()", setup="from __main__ import test_func"))
```


## Profiler 
```python
def test_func():
  # the code to be tested
    arr = []
    for i in range(500):
        arr.append(i)

if __name__ == '__main__':
    import cProfile
    cProfile.run("test_func()")
```

```command
504 function calls in 0.000 seconds

  Ordered by: standard name

  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <iPython-input-11-6e0e08304ab5>:1(test_func)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## %%time
```python
%%time

def test_func():
  # the code to be tested
    arr = []
    for i in range(500):
        arr.append(i)

if __name__ == '__main__':
    test_func()
```

```command
CPU times: user 86 µs, sys: 2 µs, total: 88 µs
Wall time: 93 µs
```

## Use the Latest Version of Python

## Use Application Performance Monitoring Tools
- There are several great APM providers available out there, with [ScoutAPM](https://scoutapm.com/) being just one solution.

## Import Modules Lazily Wherever Possible

## Use Built-In Functions 

## Avoid Global Variables
```python
x = "Hello World!"

def test_func_glob():
    arr = []
    for i in range(50):
      arr.append(x)

def test_func_loc():
    x = "Hello World!"
    arr = []
    for i in range(50):
      arr.append(x)

if __name__ == '__main__':
    import timeit
    print("Global -> ", timeit.timeit("test_func_glob()", setup="from __main__ import test_func_glob"))
    print("Local -> ", timeit.timeit("test_func_loc()", setup="from __main__ import test_func_loc"))
```

```command
Global ->  4.058157788000017
Local ->  3.613330179000002
```

## Prefer NumPy Arrays Over Traditional Lists

## Use List Comprehension
```python
result = []
for n in range(0, 20):
    result.append(n**2)
```

```python
# Here’s how you can do it with a list comprehension
result = [n**2 for n in range(0, 20)]
```

## Avoid Checking if a Variable is True
```python
str = "Hey there!"

# The traditional way
if str != None:
  print("Found")
else:
  print("Not Found")

# The faster way
if str:
  print("Found")
else:
  print("Not Found")
```

## Put Loop Inside Functions, Rather Than Otherwise

## Prefer Enumerate For Value and Index
```python
arr = range(0, 20)

for i in range(len(arr)):
  print("Index", i)
  print("Value", arr[i])
```

```python
arr = range(0, 20)

for i, number in enumerate(arr):
  print("Index", i)
  print("Value", number)
```

## Use In Over Iteration
```python
arr = [] # Your list of elements

if (query in arr):
  # Match found
else:
  # Match not found
```

## Count Unique Values Using Counter
```python
val_counts = {}
for num in arr:
    if num in val_counts:
        val_counts[num] += 1
    else:
        val_counts[num] = 1
```

But, a better way would be to use the Counter() method from collections:
```python
val_counts = Counter(arr)
```

## Concatenate Strings With join()
```python
str1 = "Hello" + "World!" + "Foo" + "Bar" + "Baz"
# => HelloWorld!FooBarBaz

str2 = " ".join(["Hello", "World!", "Foo", "Bar", "Baz"])
# => Hello World! Foo Bar Baz
```

## Try An Alternative Way


---

## Reference
    - [15 Tips for Better Python Performance](https://scoutapm.com/blog/python-performance-tips)
    - [Google Python 編碼規範指南](https://mp.weixin.qq.com/s?__biz=MzUxMjUxMzIwNA==&mid=2247483979&idx=1&sn=d00863bec881f6729f29d4b0f62ba1a9&chksm=f9620790ce158e86249e2a86a9ca6e2b731ea5a9c44ffc76c4a54668c699c9df8a30aa9bba25&scene=21#wechat_redirect)