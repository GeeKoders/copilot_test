from is_prime_algorithm import zzz

# test_is_prime_algorithm.py


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_all_elements_are_prime():
    for num in zzz:
        assert is_prime(num), f"{num} is not prime"

def test_contains_all_primes_2_to_99():
    expected_primes = [n for n in range(2, 100) if is_prime(n)]
    assert zzz == expected_primes

def test_no_duplicates():
    assert len(zzz) == len(set(zzz)), "Duplicates found in zzz"

def test_first_10_primes():
    expected_first_10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert zzz[:10] == expected_first_10

def test_length_of_zzz():
    assert len(zzz) == 25, f"Expected 25 primes, got {len(zzz)}"