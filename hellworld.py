a = 1
print a

t = 1, 2
a, b = t

l = [1, 2, 3, 'hello']
l.append(4)

d = {'hello': 'world', 'hi': 'Anna'}

for i in l:
    print i

for i in d:
    print i, d[i]

for k, v in d.items():
    print k, v


def f(x, y):
    return x + y, 1

w, z = f(1, 2)
print w, z


class A:
    def __init__(self, i, r):
        self.a = i
        self.b = r


    def method(self):
        return self.a + str(self.b)

a = A('str',1)
print a.method()


