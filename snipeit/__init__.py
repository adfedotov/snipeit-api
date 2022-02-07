from SnipeIT import SnipeIT

test = SnipeIT('a', 'b')

r = test.assets.get(limit=2, search='123')
print(r)
