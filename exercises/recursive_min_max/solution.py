SUBMIT = False


def recursive_min_max(
    lst: list[int], low: int = 0, high: int | None = None
) -> tuple[int, int]:
    """Recursive Min/Max"""
    pass


def test() -> None:
    """Simple self-test for Recursive Min/Max."""
    assert recursive_min_max([3, 1, 4, 1, 5, 9]) == (1, 9), (
        f"Expected (1, 9), got {recursive_min_max([3, 1, 4, 1, 5, 9])}"
    )
    assert recursive_min_max([42]) == (42, 42), (
        f"Expected (42, 42), got {recursive_min_max([42])}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
