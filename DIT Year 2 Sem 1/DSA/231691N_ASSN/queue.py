# class Queue:
#     def __init__(self, maxSize):
#         self._count = 0
#         self._front = 0
#         self._back = maxSize - 1
#         self._qArray = [None] * maxSize
#
#     def isEmpty(self):
#         return self._count == 0
#
#     def isFull(self):
#         return self._count == len(self._qArray)
#
#     def __len__(self):
#         return self._count
#
#     def enqueue(self, item):
#         assert not self.isFull(), "Cannot enqueue to a full queue."
#         self._back = (self._back + 1) % len(self._qArray)
#         self._qArray[self._back] = item
#         self._count += 1
#
#     def dequeue(self):
#         assert not self.isEmpty(), "Cannot dequeue from an empty queue."
#         item = self._qArray[self._front]
#         self._qArray[self._front] = None
#         self._front = (self._front + 1) % len(self._qArray)
#         self._count -= 1
#         return item
#
#     def __str__(self):
#         maxSize = len(self._qArray)
#         outStr = ""
#         for i in range(self._count):
#             outStr += "[" + str((self._front + i) % maxSize) + "]:"
#             outStr += str(self._qArray[(self._front + i) % maxSize].prod_id) + " "
#         return outStr
#

class Queue:
    def __init__(self):
        self.qList = list()

    def isEmpty(self):
        return len(self.qList) == 0

    def __len__(self):
        return len(self.qList)

    def enqueue(self, item):
        self.qList.append(item)

    def dequeue(self):
        assert not self.isEmpty(), \
            "Cannot dequeue from an empty queue."
        return self.qList.pop(0)
