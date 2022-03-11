import re
from pathlib import Path


def read_input() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        input = [x.strip() for x in stream.readlines()]
    return input


def gate(operator: str, values: list[int]) -> int:
    if operator == "AND":
        return values[0] & values[1]
    elif operator == "OR":
        return values[0] | values[1]
    elif operator == "LSHIFT":
        return values[0] << values[1]
    elif operator == "RSHIFT":
        return values[0] >> values[1]
    elif operator == "NOT":
        return 0xFFFF & ~values[0]


def solution(input: list[str]) -> dict[str, int]:
    regex = r"(?:(.*?)(OR|NOT|RSHIFT|LSHIFT|AND) (.*)|(.*)) -> (.*)"
    output = {}
    index = 0
    while len(input) > 0:
        match = re.search(regex, input[index])
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
                if type(value) == str and value not in output:
                    wait = True
            if not wait:
                output[result_key] = gate(
                    operator=match.group(2),
                    values=[x if type(x) == int else output[x] for x in values],
                )
                input.remove(input[index])
        else:
            try:
                value = int(match.group(4))
            except ValueError:
                value = match.group(4)
            if type(value) == int:
                output[result_key] = value
                input.remove(input[index])
            elif type(value) == str and value in output:
                output[result_key] = output[value]
                input.remove(input[index])

        if index < len(input) - 1:
            index += 1
        else:
            index = 0
    return output


def main():
    if not (input := read_input()):
        return

    signal = solution(input=input)
    print(f"Part One: {signal['a']}")


# region testing
def examples():
    signal = solution(
        input=[
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
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
    examples()
    main()
