import itertools

first_6_primes = [2, 3, 5, 7, 11, 13]

class Prime6:    

    class _Prime6_iter:
        def __init__(self):
            self.i = 0
            self.primes = first_6_primes
        
        def __next__(self):
            if self.i >= 6:
                raise StopIteration()
            else:
                j = self.i
                self.i += 1
                return self.primes[j]

    def __iter__(self):
        return Prime6._Prime6_iter()
p6 = Prime6()

for p in p6:
    print(p)

print(list(p6))
