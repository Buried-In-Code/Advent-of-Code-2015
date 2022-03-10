from pathlib import Path
from hashlib import md5

def read_input() -> str | None:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return None
    with input_file.open("r", encoding="UTF-8") as stream:
        input = stream.read()
    return input

def solution(input: str) -> int:
    counter = 1
    while not md5(f"{input}{counter}".encode()).hexdigest().startswith("00000"):
        counter += 1
    return counter

def main():
    if not (input := read_input()):
        return
    
    number = solution(input=input)
    print(f"Part One: {number}")

# region testing
def examples():
    number = solution(input="abcdef")
    assert number == 609043
    number = solution(input="pqrstuv")
    assert number == 1048970
# endregion

if __name__ == "__main__":
    examples()
    main()