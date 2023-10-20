from hashlib import md5
from pathlib import Path

from rich import print
from rich.traceback import install


def read_input_file() -> str | None:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return None
    with input_file.open("r", encoding="UTF-8") as stream:
        return stream.read()


def solution(input_data: str) -> int:
    counter = 1
    while not md5(f"{input_data}{counter}".encode()).hexdigest().startswith("000000"):  # noqa: S324
        counter += 1
    return counter


def main() -> None:
    if not (input_data := read_input_file()):
        return

    number = solution(input_data=input_data)
    print(f"Part Two: {number}")


# region testing
def examples() -> None:
    pass


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
