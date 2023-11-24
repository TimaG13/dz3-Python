def prime_generator(end):
    primes = []  # Зберігатиме прості числа
    current = 2   # Починаємо з першого простого числа

    while current <= end:
        # Перевірка, чи поточне число є простим
        is_prime = all(current % prime != 0 for prime in primes)
        if is_prime:
            primes.append(current)
            yield current

        current += 1

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
