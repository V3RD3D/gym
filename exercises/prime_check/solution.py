SUBMIT = False


def prime_check(_n: int) -> bool:
    # noqa: ARG001
    """Checks if a number is prime.

    Example usage:
    >>> prime_check(2)
    True
    >>> prime_check(4)
    False
    >>> prime_check(17)
    True
    """
    return False


def test() -> None:
    """Simple self-test for Primality Test."""
    cases = {2: True, 4: False, 17: True, 1: False, 0: False, 97: True}
    for n, expected in cases.items():
        try:
            res = prime_check(n)
            assert res == expected, f"Failed for n={n}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
