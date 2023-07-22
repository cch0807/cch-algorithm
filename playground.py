<<<<<<< HEAD
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
=======
def solution(n):
    if n == 0:  # n이 0인 경우, 드래곤과 알이 없으므로 0을 반환
        return 1

    dragons = []
    eggs = [0]x

    for _ in range(n + 1):
        for i in range(len(eggs)):
            if eggs[i] == 2:
                dragons.append(0)
                eggs[i] += 1
            elif eggs[i] < 2:
                eggs[i] += 1

        for i in range(len(dragons)):
            if dragons[i] < 4:
                dragons[i] += 1
                eggs.append(0)

    return len(dragons) + len(eggs) - 1  # 드래곤의 수와 알의 수를 합하여 반환


print(solution(4))
>>>>>>> 41c429841c3bb8d7bfc62b31dbc6ad142b268137
