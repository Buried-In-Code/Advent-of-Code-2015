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


def main() -> None:
    if not (input_data := read_input_file()):
        return

    count = solution(input_data=input_data)
    print(f"Part One: {count}")


# region testing
def examples() -> None:
    count = solution(input_data=["ugknbfddgicrmopn"])
    assert count == 1
    count = solution(input_data=["aaa"])
    assert count == 1
    count = solution(input_data=["jchzalrnumimnmhp"])
    assert count == 0
    count = solution(input_data=["haegwjzuvuyypxyu"])
    assert count == 0
    count = solution(input_data=["dvszwmarrgswjxmb"])
    assert count == 0


# endregion

if __name__ == "__main__":
    examples()
    main()
