class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:

        bucket = self.map[self.hash(key)]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key: int) -> int:

        bucket = self.map[self.hash(key)]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:

        bucket = self.map[self.hash(key)]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return