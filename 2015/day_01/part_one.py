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
    for entry in input:
        if entry == "(":
            total += 1
        elif entry == ")":
            total -= 1
    return total


def main():
    if not (input := read_input()):
        return

    floor = solution(input=input)
    print(f"Part One: {floor}")


# region testing
def examples():
    floor = solution(input="(())")
    assert floor == 0
    floor = solution(input="()()")
    assert floor == 0
    floor = solution(input="(((")
    assert floor == 3
    floor = solution(input="(()(()(")
    assert floor == 3
    floor = solution(input="))(((((")
    assert floor == 3
    floor = solution(input="())")
    assert floor == -1
    floor = solution(input="))(")
    assert floor == -1
    floor = solution(input=")))")
    assert floor == -3
    floor = solution(input=")())())")
    assert floor == -3


# endregion

if __name__ == "__main__":
    examples()
    main()
