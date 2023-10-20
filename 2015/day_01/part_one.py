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
    for entry in input_data:
        if entry == "(":
            total += 1
        elif entry == ")":
            total -= 1
    return total


def main() -> None:
    if not (input_data := read_input_file()):
        return

    floor = solution(input_data=input_data)
    print(f"Part One: {floor}")


# region testing
def examples() -> None:
    floor = solution(input_data="(())")
    assert floor == 0
    floor = solution(input_data="()()")
    assert floor == 0
    floor = solution(input_data="(((")
    assert floor == 3
    floor = solution(input_data="(()(()(")
    assert floor == 3
    floor = solution(input_data="))(((((")
    assert floor == 3
    floor = solution(input_data="())")
    assert floor == -1
    floor = solution(input_data="))(")
    assert floor == -1
    floor = solution(input_data=")))")
    assert floor == -3
    floor = solution(input_data=")())())")
    assert floor == -3


# endregion

if __name__ == "__main__":
    examples()
    main()
