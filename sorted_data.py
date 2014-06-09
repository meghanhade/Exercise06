def main():
    ratings = open('scores.txt')

    x = 0
    restaurants = []
    for line in ratings:
        line = line.rstrip()
        restaurants.append(line)
        x += 1

    restaurants.sort()
    for each in restaurants:
        print each


if __name__ == "__main__":
    main()