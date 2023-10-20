from pathlib import Path


def read_input_file() -> str | None:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return None
    with input_file.open("r", encoding="UTF-8") as stream:
        return stream.read()


def solution(input_data: str) -> int:
    total = 0
    for index, entry in enumerate(input_data):
        if entry == "(":
            total += 1
        elif entry == ")":
            total -= 1
        if total < 0:
            return index + 1
    return 0


def main() -> None:
    if not (input_data := read_input_file()):
        return

    step = solution(input_data=input_data)
    print(f"Part Two: {step}")


# region testing
def examples() -> None:
    step = solution(input_data=")")
    assert step == 1
    step = solution(input_data="()())")
    assert step == 5


# endregion

if __name__ == "__main__":
    examples()
    main()
