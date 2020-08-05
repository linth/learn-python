

class A:
    total = 3123435123


class B(A):
    pass


class C(A):
    pass


class M:
    def print_total(self):
        """
        print the variable of total.
        :return:
        """
        print(self.total)

    def to_list(self):
        """
        convert to list.
        :return:
        """
        l = list()
        l.append(self.total)
        return l


class D(B, M):
    pass


class E(C, M):
    pass


if __name__ == '__main__':
    e = E()
    e.print_total()
    print(e.to_list())
