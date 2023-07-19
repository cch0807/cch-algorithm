def sugar_delivery(weight):
    for bag5 in range(weight // 5, -1, -1):
        remainder = weight - bag5 * 5
        if remainder % 3 == 0:
            bag3 = remainder // 3
            return bag5 + bag3

    return -1


if __name__ == "__main__":
    weight = int(input())
    result = sugar_delivery(weight)
    print(result)
