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
    count = 0
    for word in input:
        word = word.lower()
        match = False
        for x in range(0, len(word)):
            group = word[x : x + 2]
            leftover = word[x + 2 :]
            if group in leftover:
                match = True
        if not match:
            continue
        match = False
        for index, letter in enumerate(word):
            if index + 2 >= len(word):
                break
            if letter == word[index + 2]:
                match = True
        if not match:
            continue
        count += 1
    return count


def main():
    if not (input := read_input()):
        return

    count = solution(input=input)
    print(f"Part Two: {count}")


# region testing
def examples():
    count = solution(input=["qjhvhtzxzqqjkmpb"])
    assert count == 1
    count = solution(input=["xxyxx"])
    assert count == 1
    count = solution(input=["uurcxstgmygtbstg"])
    assert count == 0
    count = solution(input=["ieodomkazucvgmuy"])
    assert count == 0


# endregion

if __name__ == "__main__":
    examples()
    main()
