import math
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
    total = 0
    for dimension_str in input:
        dimensions = [int(x) for x in dimension_str.split("x")]
        max_ = max(dimensions)
        ribbon = sum([x*2 for x in dimensions]) - max_*2
        ribbon += math.prod(dimensions)
        total += ribbon
    return total

def main():
    if not (input := read_input()):
        return
    
    ribbon = solution(input=input)
    print(f"Part Two: {ribbon}")

# region testing
def examples():
    ribbon = solution(input=["2x3x4"])
    assert ribbon == 34
    ribbon = solution(input=["1x1x10"])
    assert ribbon == 14
# endregion

if __name__ == "__main__":
    examples()
    main()