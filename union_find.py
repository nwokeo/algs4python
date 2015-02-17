#union find
class UF:
    def __init__(self, n):
        self.n = n

    def union(self, p, q):
        pass

    def connection(self, p, q):  # bool
        pass

    def find(self, p):  # int
        pass

    def count(self):  # int
        pass

    def connected(self, p, q):
        pass


#quick find (eager)
class QuickFindUF:
    def __init__(self, n):
        self.n = n
        self.a = []

    def quickfind(self):  # set id of each object to itself
        for i in range(self.n):
            #a[i] = i
            self.a.append(i)
        return self.a  # allow visualization

    def connected(self, p, q):
        return self.a[p] == self.a[q]

    def union(self, p, q):
        pid = self.a[p]  # find ids
        qid = self.a[q]
        for i in range(len(self.a)):
            if self.a[i] == pid:
                self.a[i] = qid  # change entries that are the same
        return self.a


#quick union (lazy)
class QuickUnionUF:
    def __init__(self, n):
        self.n = n
        self.a = []

    def quickunion(self):  # set id of each object to itself
        for i in range(self.n):
            self.a.append(i)
        return self.a  # allow visualization

    def root(self, i):
        while i != self.a[i]:  # chase parents until root
            i = self.a[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.a[i] = j


#quick union (weighted)
class WeightedQuickUnionUF:
    def __init__(self, n):
        self.n = n
        self.a = []
        self.sz = [1] * n  # count the number of objects in tree rooted at i
        self.count = n

    def quickunion(self):  # set id of each object to itself
        for i in range(self.n):
            self.a.append(i)
        return self.a  # allow visualization

    def root(self, i):
        while i != self.a[i]:  # chase parents until root
            i = self.a[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:  # check sizes, link root of smaller to root of larger tree
            self.a[i] = j  # change [a] link
            self.sz[j] += self.sz[i]  # change size array
        else:
            self.a[j] = i
            self.sz[i] += self.sz[j]
        self.count -= 1  # why do i need to decrement here?


#dynamic connectivity client
def test():
    f = open('C:\\foo.txt', 'r+')
    n = int(f.readline())
    print "Number of Values: %s" % n

    uf = UF(n)

    for value in f.readlines():
        value = value.split(',')
        print value[0], value[1]
        p = value[0]
        q = value[1]

        if not uf.connected(p, q):
            uf.union(p, q)
            print p + ' ' + q


# Test QF
def testqf():
    qf = QuickFindUF(10)
    print qf.quickfind()
    #ex1.1
    qf.union(4, 9)
    qf.union(7, 8)
    qf.union(1, 6)
    qf.union(3, 0)
    qf.union(1, 8)
    print qf.union(0, 5)
    #print qf.connected(1, 2)
    #print qf.connected(0, 4)
    #print qf.connected(1, 5)


# Test QU
def testqu():
    qu = QuickUnionUF(10)
    print qu.quickunion()
    qu.union(0, 1)
    qu.union(1, 2)
    qu.union(2, 3)
    qu.union(3, 4)
    print qu.connected(1, 2)
    print qu.connected(0, 4)
    print qu.connected(1, 5)


# Test weighted QU
def testweightedqu():
    wqu = WeightedQuickUnionUF(10)
    print 'original array ', wqu.quickunion()
    '''
    wqu.union(4, 3)
    wqu.union(3, 8)
    wqu.union(6, 5)
    wqu.union(9, 4)
    wqu.union(2, 1)
    wqu.union(5, 0)
    wqu.union(7, 2)
    wqu.union(6, 1)
    wqu.union(7, 3)
    print wqu.sz
    '''
    #ex1.2
    wqu.union(5,7)
    wqu.union(9,3)
    wqu.union(9,6)
    wqu.union(2,0)
    wqu.union(0,5)
    wqu.union(1,9)
    wqu.union(8,9)
    wqu.union(5,3)
    wqu.union(2,4)
    print 'finished array ', wqu.a
    #print wqu.connected(1, 2)
    #print wqu.connected(0, 4)
    #print wqu.connected(1, 5)

testweightedqu()
