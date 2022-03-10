from .day_01 import part_one as day_01_part_one
from .day_01 import part_two as day_01_part_two
from .day_02 import part_one as day_02_part_one
from .day_02 import part_two as day_02_part_two
from .day_03 import part_one as day_03_part_one
from .day_03 import part_two as day_03_part_two
from .day_04 import part_one as day_04_part_one
from .day_04 import part_two as day_04_part_two
from .day_05 import part_one as day_05_part_one


def main():
    print("Day #1")
    day_01_part_one.examples()
    day_01_part_one.main()
    day_01_part_two.examples()
    day_01_part_two.main()

    print("---")
    print("Day #2")
    day_02_part_one.examples()
    day_02_part_one.main()
    day_02_part_two.examples()
    day_02_part_two.main()

    print("---")
    print("Day #3")
    day_03_part_one.examples()
    day_03_part_one.main()
    day_03_part_two.examples()
    day_03_part_two.main()

    print("---")
    print("Day #4")
    day_04_part_one.examples()
    day_04_part_one.main()
    day_04_part_two.examples()
    day_04_part_two.main()

    print("---")
    print("Day #5")
    day_05_part_one.examples()
    day_05_part_one.main()


if __name__ == "__main__":
    main()
