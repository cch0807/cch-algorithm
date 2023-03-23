# List
- 순서가 중요한 자료구조
- python에서 사용하는 list는 array list(Dynamic array) 이다.

# Array list
- Array / Dynamic array

# (static) array
- 배열의 특성
    - 1. 고정된 저장 공간(fixed-size)
    - 2. 순차적인 데이터 저장(order)
- 배열은 선언시에 size를 정하여 해당 size만큼의 연속된 메모리를 할당 받아 data를 연속적/순차적으로 저장하는 자료구조이다.

    int arr[5] = {3, 7, 4, 2, 6} //size가 5인 int형 배열 선언

- 위의 예시에서는 배열의 size를 5로 정했기 때문에 int형 데이터(4 byte) 5개를 저장할 메모리 공간인 20 Byte를 미리 할당을 받는다. 이처럼 고정된 size를 갖게 되기 때문에 static array라고 부르기도 한다.
- 4byte(int형 데이터) * 5(size) = 20byte
- 또한 배열의 데이터를 연속적이고 순차적으로 메모리에 저장한다.

# Random access
- 메모리에 저장된 데이터에 접근하려면 주소값을 알아야 한다. 배열변수는 자신이 할당받은 메모리의 첫 번째 주소값을 가리킨다. 배열은 연속적/순차적으로 저장되어 있기 때문에 첫 주소값만 알고 있다면 index에도 즉시 접근이 가능하다. 이를 direct access 또는 random access라고 부른다. 첫 번째 데이터가 저장된 주소값이 0x4AF55라면 2번째 데이터는 0x4AF55 + 4*1에 저장되어 있을 것이다. 아무리 긴 배열이더라도 한번의 연산으로 원하는 데이터에 바로 접근할 수 있다. 즉 O(1)의 시간복잡도를 갖는다.
- linked list는 메모리상에서 연속적/순차적으로 저장되어 있지 않기 때문에 random access는 불가능하다. n번 째 데이터에 접근하기 위해서 array는 1번의 연산만 해도 되지만(O(1)), linked list는 n번의 연산을 해야 하기 때문에 시간복잡도는 O(n)이 된다.

# static array 한계
- 데이터의 갯수가 정해져 있는 경우에는 static array를 사용하는 것이 매우 효율적이다. 하지만 선언시에 정한 size보다 더 많은 데이터를 저장해야 하는 경우 공간이 남아있지 않아서 문제가 발생할 수 있다. 그렇다고 매번 크기가 엄청 큰 배열을 선언한다면 그만큼 메모리 비효율이 발생하게 된다. 이런 문제점을 해결할 수 있는 것이 바로 dynamic array 이다.

# Dynamic array (동적 배열)
- 선언 이후에 size를 변경할 수 없는(Static Array)과 다르게 동적배열(Dynamic Array)는 size를 늘릴 수 있다.

- 동적배열(dynamic array)은 배열의 크기(size)를 변경(resizing)할 수 있는 배열이다. fixed-size인 Static Array의 한계점을 보안하고자 고안되었다. 동적배열에 데이터를 계속 추가하다가 기존에 할당된 size를 초과하게 되면, size를 늘린 배열을 새로 선언하고 그곳으로 모든 데이터를 옮긴다. 그리고 기존의 배열은 메모리에서 삭제(free)한다. 이 과정을 resize라고 한다. resize를 한칸씩 늘린다면 비효율적이므로 일반적으로 2배 큰 크기로 resize한다. 이를 더블링(Doubling)이라고 한다. resize 덕분에 데이터를 추가 저장할 수 있게된다.

# Dynamic Array 사용법
- 선언시에 배열의 크기를 정하지 않아도 되기 때문에 코딩테스트에서 dynamic array를 자주 사용하게 된다. Python에서는 list 자료형을 통해 dynamic array을 이미 잘 구현해 두었기 때문에 직접 구현할 필요 없이 사용할 수 있다.

- 즉 문제에서 배열을 사용해야 하는 경우에는 list를 선언하여 사용하면 된다. 우리가 익혀야 할 것은 list의 연산(operation)들과 시간복잡도이다.


# Linked list
- Node

