def main():
    band_name = band_name_generator()
    print(band_name)


def band_name_generator():
    print("Welcome to the Band Name Generator.")
    hometown = input("What city did you grow up in?\n")
    pet_name = input("What was the name of your first pet?\n")
    return f"Your band name could be: {hometown} {pet_name}"


if __name__ == "__main__":
    main()
