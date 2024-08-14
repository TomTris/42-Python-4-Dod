def callLimit(limit: int):
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if (count < limit):
                count += 1
                val = function()
                return val
            else:
                print(f"{function} call to many times")
                return None
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
