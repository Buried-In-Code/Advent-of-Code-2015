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
        if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
            continue
        vowels = (
            word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
        )
        if vowels < 3:
            continue
        previous = ""
        letter_count = 0
        valid = False
        for letter in word:
            if letter == previous:
                letter_count += 1
            else:
                letter_count = 1
            if letter_count >= 2:
                valid = True
                break
            previous = letter
        if not valid:
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
    count = solution(input=["ugknbfddgicrmopn"])
    assert count == 1
    count = solution(input=["aaa"])
    assert count == 1
    count = solution(input=["jchzalrnumimnmhp"])
    assert count == 0
    count = solution(input=["haegwjzuvuyypxyu"])
    assert count == 0
    count = solution(input=["dvszwmarrgswjxmb"])
    assert count == 0


# endregion

if __name__ == "__main__":
    examples()
    main()
