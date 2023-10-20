import re
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


def gate(operator: str, values: list[int]) -> int | None:
    if operator == "AND":
        return values[0] & values[1]
    if operator == "OR":
        return values[0] | values[1]
    if operator == "LSHIFT":
        return values[0] << values[1]
    if operator == "RSHIFT":
        return values[0] >> values[1]
    if operator == "NOT":
        return 0xFFFF & ~values[0]
    return None


def solution(input_data: list[str]) -> dict[str, int]:
    regex = r"(?:(.*?)(OR|NOT|RSHIFT|LSHIFT|AND) (.*)|(.*)) -> (.*)"
    output = {}
    index = 0
    while len(input_data) > 0:
        match = re.search(regex, input_data[index])
        if not match:
            break
        result_key = match.group(5)

        if match.group(2):
            values = []
            if match.group(1):
                try:
                    values.append(int(match.group(1).strip()))
                except ValueError:
                    values.append(match.group(1).strip())
            try:
                values.append(int(match.group(3).strip()))
            except ValueError:
                values.append(match.group(3).strip())
            wait = False
            for value in values:
                if isinstance(value, str) and value not in output:
                    wait = True
            if not wait:
                output[result_key] = gate(
                    operator=match.group(2),
                    values=[x if isinstance(x, int) else output[x] for x in values],
                )
                input_data.remove(input_data[index])
        else:
            try:
                value = int(match.group(4))
            except ValueError:
                value = match.group(4)
            if isinstance(value, int):
                output[result_key] = value
                input_data.remove(input_data[index])
            elif isinstance(value, str) and value in output:
                output[result_key] = output[value]
                input_data.remove(input_data[index])

        if index < len(input_data) - 1:
            index += 1
        else:
            index = 0
    return output


def main() -> None:
    if not (input_data := read_input_file()):
        return

    signal = solution(input_data=input_data)
    print(f"Part One: {signal['a']}")


# region testing
def examples() -> None:
    signal = solution(
        input_data=[
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ],
    )
    assert signal == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }


# endregion

if __name__ == "__main__":
    install(show_locals=True, max_frames=5)
    examples()
    main()
