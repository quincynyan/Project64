def main():
    for i in range(2, 13):
        for j in range(1, 13):
            print("{:>2} times {:>2} is {:>3}".format(j, i, j*i))
        print("-" * 20)


if(__name__ == "__main__"):
    main()
