import random

QUOTES = [
    {"quote": "May the Force be with you.", "movie": "Star Wars", "year": 1977},
    {"quote": "I'll be back.", "movie": "The Terminator", "year": 1984},
    {"quote": "Here's looking at you, kid.", "movie": "Casablanca", "year": 1942},
    {"quote": "You're gonna need a bigger boat.", "movie": "Jaws", "year": 1975},
    {"quote": "There's no place like home.", "movie": "The Wizard of Oz", "year": 1939},
    {"quote": "I see dead people.", "movie": "The Sixth Sense", "year": 1999},
    {"quote": "Houston, we have a problem.", "movie": "Apollo 13", "year": 1995},
    {"quote": "To infinity and beyond!", "movie": "Toy Story", "year": 1995},
]


def show(q):
    print(f'"{q["quote"]}" - {q["movie"]} ({q["year"]})')


def main():
    print("Welcome to the Movie Quote CLI!")
    print("  1 - Random quote")
    print("  2 - All quotes")
    print("  q - Quit")

    while True:
        try:
            choice = input("\nChoose an option: ").strip().lower()
        except EOFError:
            print("\nNo input available. Run with -it for interactive mode.")
            break

        if choice == "1":
            show(random.choice(QUOTES))
        elif choice == "2":
            for q in QUOTES:
                show(q)
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Enter 1, 2 or q.")


if __name__ == "__main__":
    main()

    