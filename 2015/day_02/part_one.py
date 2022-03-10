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
        length, width, height = [int(x) for x in dimension_str.split("x")]
        
        paper = (2*length*width) + (2*width*height) + (2*height*length)
        paper += min(length*width, width*height, height*length)
        total += paper
    return total

def main():
    if not (input := read_input()):
        return
    
    paper = solution(input=input)
    print(f"Part One: {paper}")

# region testing
def examples():
    paper = solution(input=["2x3x4"])
    assert paper == 58
    paper = solution(input=["1x1x10"])
    assert paper == 43
# endregion

if __name__ == "__main__":
    examples()
    main()