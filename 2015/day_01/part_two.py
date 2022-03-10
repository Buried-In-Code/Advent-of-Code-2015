from pathlib import Path


def read_input() -> str | None:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return None
    with input_file.open("r", encoding="UTF-8") as stream:
        input = stream.read()
    return input


def solution(input: str) -> int:
    total = 0
    for index, entry in enumerate(input):
        if entry == "(":
            total += 1
        elif entry == ")":
            total -= 1
        if total < 0:
            return index + 1
    return 0


def main():
    if not (input := read_input()):
        return

    step = solution(input=input)
    print(f"Part Two: {step}")


# region testing
def examples():
    step = solution(input=")")
    assert step == 1
    step = solution(input="()())")
    assert step == 5


# endregion

if __name__ == "__main__":
    examples()
    main()
