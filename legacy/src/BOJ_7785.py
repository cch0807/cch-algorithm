# 입력
n = int(input())
enter_history = []
leave_history = []
for _ in range(n):
    some = str(input()).split(" ")
    enter_history.append(some[0])

print(enter_history)


def main() -> str:
    pass


if __name__ == "__main__":
    main()
