from statistics import ft_statistics


def main():
    """
    Test the ft_statistics function with various input examples.
    """
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean",
                      tutu="median", tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474,
                      48575, hello="std", world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                      ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except Exception:
        print("ERROR")


if __name__ == "__main__":
    main()
