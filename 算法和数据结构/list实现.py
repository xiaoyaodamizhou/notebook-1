def log(*args, **kwargs):
    print(*args, **kwargs)


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.next = None
        self.tail = None
        self.length = 0

    def last_node(self):
        return self.tail

    # 返回第n个节点
    def kth_node(self, n):
        if n >= self.length:
            raise "index out of range"
        if n < 0:
            raise "index not exsit"
        p = self.next
        i = 0
        while i != n:
            p = p.next
            i += 1
        return p

    def n_last(self, n):
        index = self.length - n - 1
        return self.kth_node(index)

    def has_val(self, val):
        r = self.logged()
        if val not in r:
            return False
        return True

    def append(self, val):
        node = ListNode(val)
        self.length += 1
        if self.next is None:
            # log('test1', node.val)
            self.next = node
            self.tail = node
        else:
            # log('test2', node.val)
            self.tail.next = node
            self.tail = node

    def delete(self, n):
        # log('delete', self.length, n)
        self.length -= 1
        p = self.next
        i = 0
        q = p
        while i != n:
            q = p
            p = p.next
            i += 1
        q.next = p.next
        # log('?', self.length, n)
        if n == self.length:
            self.tail = q
            # log('tail delete', self.tail.val, q.val)
        if self.length == 0:
            self.tail = None
            self.next = None
        del p

    def resverse(self):
        r = self.logged()
        r.reverse()
        p = self.next
        while p != self.tail.next:
            p.val = r.pop(0)
            p = p.next

    def insert(self, n, val):
        node = ListNode(val)
        self.length += 1
        p = self.next
        i = 0
        q = p
        while i != n:
            q = p
            p = p.next
            i += 1
        node.next = p
        q.next = node

    def is_palindRome(self):
        r1 = self.logged()
        r2 = r1.copy()
        r2.reverse()
        if r1 == r2:
            return True
        return False

    def remove(self):
        length = self.length
        p = self.next
        for i in range(length - 1, -1, -1):
            # log('remove', i)
            self.delete(i)

    def merge_list(self, list):
        r1 = self.logged()
        r2 = list.logged()
        r = r1 + r2
        r.sort()
        length = len(r)
        self.remove()
        for i in range(length):
            self.append(r[i])
        # log('tail', self.tail, self.length, self.next)
        # log(self.logged())

    def logged(self):
        r = [self.next.val]
        p = self.next
        while p != self.tail:
            p = p.next
            r.append(p.val)
        # log(r)
        return r


def josephus(n, k):
    if k == 1:
        print('survive:', n)
        return
    p = 0
    people = list(range(1, n + 1))
    log('people', people, n, k)
    while True:
        if len(people) == 1:
            break
        p = (p + (k - 1)) % len(people)
        print('kill:', people[p])
        del people[p]
    print('survive:', people[0])
