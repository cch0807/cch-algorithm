# Memory
- 데이터를 저장하는 장소
- 비효율적인 자료구조를 사용하면 램 메모리를 과부하 하게됨.

# List 
- 데이터를 순차적으로 나열해 놓은 집합
- Array || Linked List
- Array 는 데이터 접근이 쉽고, Linked List 는 데이터 추가 삭제가 쉽다.

# RAM
- Ram memory 전기신호를 저장할 수 있는 트랜지스터라는 작은 반도체로 이루어져있다.
- 트랜지스터에 전기가 on이면 1, off면 0이다. 이를 이용해서 binary Digit(bit) 를 표현할 수 있음.
- 2bit는 4가지 숫자를 표현
- 8bit = 1byte, 2^8가지 숫자를 표현

# RAM 메모리 할당
- int(intger)
    - 4byte

- Char(Character)
    - 1byte
    - ASCIIcode

- Array
    - continuous
    - 각각 4byte each -> 총 16byte 
    - 각 데이터는 가장 작은 address를 대표 address로 설정

- Linked List -> 
    - discontinuous
    - 불연속적으로 저장하기 때문에 value만 알고있다면 다음값이 뭔지 알수없음.
    - 다음으로 나올값의 address를 함께 저장 -> Node
    - 하나의 Node당 8byte each (value + address)
    
- https://youtu.be/JHxY08iENxs