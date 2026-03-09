SUBMIT = False


def poly_mul(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Multiplies two polynomials."""
    _poly1 = poly1
    _poly2 = poly2
    # Placeholder implementation
    return []


def test() -> None:
    """Simple self-test for Polynomial Multiplication."""
    cases = [
        (([1, 2], [3, 4]), [3, 10, 8]),
        (([1, 0, 1], [1, 1]), [1, 1, 1, 1]),
    ]
    for input_data, expected in cases:
        try:
            res = poly_mul(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
