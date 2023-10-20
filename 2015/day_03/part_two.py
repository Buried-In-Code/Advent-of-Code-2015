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
    santa_location = (0, 0)  # x, y
    robot_location = (0, 0)  # x, y
    houses = {santa_location}
    for index, entry in enumerate(input_data):
        location = santa_location if index % 2 == 0 else robot_location
        if entry == "^":
            location = (location[0], location[1] + 1)
        elif entry == ">":
            location = (location[0] + 1, location[1])
        elif entry == "v":
            location = (location[0], location[1] - 1)
        elif entry == "<":
            location = (location[0] - 1, location[1])
        houses.add(location)
        if index % 2 == 0:
            santa_location = location
        else:
            robot_location = location
    return len(houses)


def main() -> None:
    if not (input_data := read_input_file()):
        return

    houses = solution(input_data=input_data)
    print(f"Part Two: {houses}")


# region testing
def examples() -> None:
    houses = solution(input_data="^v")
    assert houses == 3
    houses = solution(input_data="^>v<")
    assert houses == 3
    houses = solution(input_data="^v^v^v^v^v")
    assert houses == 11


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
