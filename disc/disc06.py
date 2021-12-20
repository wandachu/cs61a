s1 = [1, 2, 3]
s2 = s1
# print(s1 is s2)  # should be True

s2.extend([5, 6])  # s2 is now [1, 2, 3, 5, 6]. So is s1
# print(s1[4])  # should be 6

s1.append([-1, 0, 1])  # would append the list as one element
# print(s2[5])  # would be [-1, 0, 1]

s3 = s2[:]  # create a copy list which is not the same object
# print(s3 is s2)  # False
s3.insert(3, s2.pop(3))  # insert number 5 to position 3 of s3
# print(len(s1))  # should be 5 now since we popped one off

# print(s1[4] is s3[6])  # should be True since [:] is shallow copy and this item is a list

# print(s3[s2[4][1]])  # asking for s3[0] which is 1

# print(s1[:3] is s2[:3])  # False even though s1 is s2. This creates new object copies (shallow copy)
# print(s1 is s2)  # True since s1 is s2
# print(s1[:3] == s2[:3])  # True since

s1[4].append(2) # s1 = [1, 2, 3, 6, [-1, 0, 1, 2]]
# print(s3[6][3])  # 2


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for element in s:
        if element == x:
            count += 1
    for _ in range(count):
        s.append(el)


def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for element in iterable:
        if fn(element):
            yield element


def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    need_move_a = True
    need_move_b = True
    while True:
        if need_move_a:
            res_a = next(a)
        if need_move_b:
            res_b = next(b)
        if res_a < res_b:
            yield res_a
            need_move_a = True
            need_move_b = False
        elif res_a == res_b:
            yield res_a
            need_move_a = True
            need_move_b = True
        else:
            yield res_b
            need_move_a = False
            need_move_b = True


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)