import TestA


class TestB(TestA.TestA):
    def cici(self):
        return "cici"

    def yoyo(self):
        return 'rewrite'


if __name__ == "__main__":
    b = TestB()
    print(b.haha())
    print(b.yoyo())


