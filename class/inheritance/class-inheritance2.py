

class A(object):
    def method1(self):
        print("A's method 1")

    def method2(self):
        print("A's method 2")


class B(A):
    def method3(self):
        print("B's method 3")


class C(A):
    def method2(self):
        print("C's method 2")

    def method3(self):
        print("C's method 3")


class D(B, C):
    def method4(self):
        print("D's method 4")


if __name__ == '__main__':
    d = D()
    d.method4() # found it in class D.
    d.method3() # found it in class B.
    d.method2() # found it in class C.
    d.method1() # found it in class A.
