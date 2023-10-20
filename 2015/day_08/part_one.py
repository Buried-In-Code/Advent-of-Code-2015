from pathlib import Path

from rich import print
from rich.traceback import install


def read_input_file() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        return [x.strip() for x in stream.readlines()]


def solution(input_data: list[str]) -> tuple[int, int]:
    code_count = 0
    memory_count = 0
    for entry in input_data:
        code_count += len(entry) + 2

        i = 0
        while i < len(entry):
            if entry[i] == "\\":
                if entry[i + 1] == "\\" or entry[i + 1] == '"':
                    memory_count += 1
                    i += 2
                elif entry[i + 1] == "x":
                    memory_count += 1
                    i += 4
            else:
                memory_count += 1
                i += 1
    return code_count, memory_count


def main() -> None:
    if not (input_data := read_input_file()):
        return

    count = solution(input_data=input_data)
    print(f"Part One: {count[0]}-{count[1]} = {count[0]-count[1]}")


# region testing
def examples() -> None:
    # fmt: off
    count = solution(input_data=[""])
    assert count == (2, 0)
    count = solution(input_data=["abc"])
    assert count == (5, 3)
    count = solution(input_data=["aaa\"aaa"])  # noqa: Q003
    assert count == (10, 7)
    count = solution(input_data=["\x27"])
    assert count == (6, 1)
    count = solution(input_data=["", "abc", "aaa\"aaa", "\x27"])  # noqa: Q003
    assert count == (23, 11)
    # fmt: on


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
