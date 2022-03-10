import re
from pathlib import Path


def read_input() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        input = stream.readlines()
    return input


def solution(input: list[str]) -> int:
    lights = {(x, y): False for x in range(0, 1000) for y in range(0, 1000)}
    regex = r"(.*) (\d+,\d+).*?(\d+,\d+)"
    for command in input:
        match = re.search(regex, command)
        if not match:
            continue
        state = match.group(1)
        start = tuple(int(x) for x in match.group(2).split(","))
        end = tuple(int(x) for x in match.group(3).split(","))
        temp = start
        while temp[0] <= end[0]:
            while temp[1] <= end[1]:
                if state == "turn on":
                    lights[temp] = True
                elif state == "turn off":
                    lights[temp] = False
                elif state == "toggle":
                    lights[temp] = not lights[temp]

                temp = (temp[0], temp[1] + 1)
            temp = (temp[0] + 1, start[1])
    count = sum(x for x in lights.values() if x)
    return count


def main():
    if not (input := read_input()):
        return

    count = solution(input=input)
    print(f"Part One: {count}")


# region testing
def examples():
    count = solution(input=["turn on 0,0 through 999,999"])
    assert count == 1000000
    count = solution(input=["toggle 0,0 through 999,0"])
    assert count == 1000
    count = solution(input=["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"])
    assert count == 999996


# endregion

if __name__ == "__main__":
    examples()
    main()
