class MagicList(list):
    def __init__(self, cls_type = None):
        """Initialize the class"""
        self.cls_type = cls_type
        super(MagicList, self).__init__()
        self._list = list()

    def __getitem__(self, ii):
        """Get a list item"""
        if len(self._list) == 0:
            self._list.append(self.cls_type())
        return self._list[ii]

    def __setitem__(self, ii, val):
        self._list.append("")
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

class Person:
    age: int = 1


if __name__=='__main__':
    b = MagicList()
    b[0] = 5
    print(b)
    #-------------------------------------
    b = MagicList(cls_type=Person)
    b[0].age =5
    print(b)
