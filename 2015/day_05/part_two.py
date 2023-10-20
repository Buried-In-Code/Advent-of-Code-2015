from pathlib import Path


def read_input_file() -> list[str]:
    input_file = Path(__file__).parent / "input.txt"
    if not input_file.exists():
        print(f"{input_file} doesn't exist")
        return []
    with input_file.open("r", encoding="UTF-8") as stream:
        return stream.readlines()


def solution(input_data: list[str]) -> int:
    count = 0
    for word in input_data:
        word = word.lower()  # noqa: PLW2901
        match = False
        for x in range(len(word)):
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


def main() -> None:
    if not (input_data := read_input_file()):
        return

    count = solution(input_data=input_data)
    print(f"Part Two: {count}")


# region testing
def examples() -> None:
    count = solution(input_data=["qjhvhtzxzqqjkmpb"])
    assert count == 1
    count = solution(input_data=["xxyxx"])
    assert count == 1
    count = solution(input_data=["uurcxstgmygtbstg"])
    assert count == 0
    count = solution(input_data=["ieodomkazucvgmuy"])
    assert count == 0


# endregion

if __name__ == "__main__":
    examples()
    main()
