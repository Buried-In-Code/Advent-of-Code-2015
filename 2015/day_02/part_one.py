from pathlib import Path

from rich import print
from rich.traceback import install


def read_input_file() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        return stream.readlines()


def solution(input_data: list[str]) -> int:
    total = 0
    for dimension_str in input_data:
        length, width, height = (int(x) for x in dimension_str.split("x"))

        paper = (2 * length * width) + (2 * width * height) + (2 * height * length)
        paper += min(length * width, width * height, height * length)
        total += paper
    return total


def main() -> None:
    if not (input_data := read_input_file()):
        return

    paper = solution(input_data=input_data)
    print(f"Part One: {paper}")


# region testing
def examples() -> None:
    paper = solution(input_data=["2x3x4"])
    assert paper == 58
    paper = solution(input_data=["1x1x10"])
    assert paper == 43


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
