
def print_heart():
    heart = [
        "  ❤️❤️❤️  ",   
            "💌",
    ]
    for line in heart:
        print(line)

def main():
    hearts_number = 5

    for _ in range(hearts_number):
        print_heart()
        print()

    print("Eu te amo💌")

if __name__ == "__main__":
    main()

