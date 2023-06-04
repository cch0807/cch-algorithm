# UserDict / UserList / UserString
# 문제 없이 메서드를 오버라이드할 수 있기 때문에 dict, list, str을 상속하는 것보다 UserDict, UserList, UserString을 상속하는 것이 좋다.
# 그러나 간단하게 사용할 때에는 dict, list, str을 상속받아 사용.

from collections import UserDict, UserList, UserString


class CustomDict(UserDict):
    def contain_value(self, values):
        return values in self.data.values()
