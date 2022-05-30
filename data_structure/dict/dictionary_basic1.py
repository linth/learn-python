"""
References:
    - https://realpython.com/python-dicts/
"""

MLB_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)


if __name__ == '__main__':
    d = {0: 'a', 1: 'b', 2: 'c', 3: 'd', '5': 'ddd'}
    e = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
    print(d)
    print(d[3], d[2], d['5'])

    print(d[0] == d[1] == d[2]) # False
    print(e[0] == e[1] == e[2]) # True

    d.clear()
    print(d)
    print(e.get(0))


