SUBMIT = False


def poly_add(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Adds two polynomials."""
    _poly1 = poly1
    _poly2 = poly2
    # Placeholder implementation: Add actual logic here.
    # For now, return an empty list to pass initial checks.
    return []


def test() -> None:
    """Simple self-test for Polynomial Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6]), (([1, 0, 1], [1, 1]), [1, 1, 1])]
    for input_data, expected in cases:
        try:
            res = poly_add(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
