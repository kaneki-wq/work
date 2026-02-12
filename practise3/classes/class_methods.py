class Counter:
    count = 0

    @classmethod
    def inc(cls):
        cls.count += 1

Counter.inc()
Counter.inc()
print(Counter.count)
