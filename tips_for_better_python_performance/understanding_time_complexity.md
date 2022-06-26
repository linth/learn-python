# time complexity with python


## Time Complexities

### Constant Time — O(1)

```python
if a > b:
    return True
else:
    return False
```

```python
def get_first(data):
    return data[0]
    
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))
```


### Logarithmic Time — O(log n)
```python
for index in range(0, len(data), 3):
    print(data[index])
```

Algorithms with logarithmic time complexity are commonly found in operations on binary trees or when using binary search.

Let’s take a look at the example of a binary search, where we need to find the position of an element in a sorted list:
```python
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
    
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))
```

### Linear Time — O(n)
```python
for value in data:
    print(value)
```

Let’s take a look at the example of a linear search, where we need to find the position of an element in an unsorted list:
```python
def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')
    
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(linear_search(data, 7))
```


### Quasilinear Time — O(n log n)
An algorithm is said to have a quasilinear time complexity when each operation in the input data have a logarithm time complexity. It is commonly seen in sorting algorithms (e.g. mergesort, timsort, heapsort).

For example: for each value in the data1 (O(n)) use the binary search (O(log n)) to search the same value in data2.

```python
for value in data1:
    result.append(binary_search(data2, value))
```

### Quadratic Time — O(n²)
```python
for x in data:
    for y in data:
        print(x, y)
```

### Exponential Time — O(2^n)
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```


### Factorial — O(n!)
```python
def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
    
if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))
```

### Important Notes
```python
def my_function(data):
    first_element = data[0]
    
    for value in data:
        print(value)
    
    for x in data:
        for y in data:
            print(x, y)
```


---

## Reference:
    - [Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)