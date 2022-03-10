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
    location = (0, 0)  # x, y
    houses = {location}
    for entry in input:
        if entry == "^":
            location = (location[0], location[1] + 1)
        elif entry == ">":
            location = (location[0] + 1, location[1])
        elif entry == "v":
            location = (location[0], location[1] - 1)
        elif entry == "<":
            location = (location[0] - 1, location[1])
        houses.add(location)
    return len(houses)


def main():
    if not (input := read_input()):
        return

    houses = solution(input=input)
    print(f"Part One: {houses}")


# region testing
def examples():
    houses = solution(input=">")
    assert houses == 2
    houses = solution(input="^>v<")
    assert houses == 4
    houses = solution(input="^v^v^v^v^v")
    assert houses == 2


# endregion

if __name__ == "__main__":
    examples()
    main()
