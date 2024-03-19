import codecs
import sys
import time

sys.setrecursionlimit(200000) #задает максимальную глубину рекурсии


class Command:
    def __init__(self, country, name, city, year, couch, score):
        self.country = country
        self.name = name
        self.city = city
        self.year = year
        self.couch = couch
        self.score = score
    
    def tmp(self):
        print(f"{self.country}, {self.name}, {self.city}, {self.year}, {self.couch}, {self.score}")


    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.country < other.country:
                return True
            elif self.country > other.country:
                return False
            else:
                if self.score < other.score:
                    return True
                elif self.score > other.score:
                    return False
                else:
                    if self.name < other.name:
                        return True
                    else:
                        return False

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.country > other.country:
                return True
            elif self.country < other.country:
                return False
            else:
                if self.score > other.score:
                    return True
                elif self.score < other.score:
                    return False
                else:
                    if self.name > other.name:
                        return True
                    else:
                        return False

    def __ge__(self, other):
        if self.year >= other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.country >= other.country:
                return True
            elif self.country < other.country:
                return False
            else:
                if self.score >= other.score:
                    return True
                elif self.score < other.score:
                    return False
                else:
                    if self.name >= other.name:
                        return True
                    else:
                        return False

    def __le__(self, other):
        if self.year <= other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.country <= other.country:
                return True
            elif self.country > other.country:
                return False
            else:
                if self.score <= other.score:
                    return True
                elif self.score > other.score:
                    return False
                else:
                    if self.name <= other.name:
                        return True
                    else:
                        return False

    def p(self):
        s = f"{self.country}, {self.name}, {self.city}, {self.year}, {self.couch}, {self.score}"
        return s



class TreeNode: #бинарное дерево
    def __init__(self, value=None, content=None): #конструктор
        self.left = None
        self.right = None
        self.value = value
        self.content = content

    def insert(self, value, content=None): #вставка нового элемента
        if self.value is None:
            self.value = value
            self.content = content
        elif value < self.value:
            if self.left is None:
                self.left = TreeNode(value, content)
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value, content)
            else:
                self.right.insert(value, content)

    def traversal(self): #проходка вывод дерева 
        if self.left:
            self.left.traversal()
        print(self.value, self.content)
        if self.right:
            self.right.traversal()

    def find(self, value): #рекурсивно ищет узел с заданным значением
        if value < self.value:
            if self.left is None:
                raise Exception('error, node content is None')
                
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                raise Exception('error, node content is None')
                
            else:
                return self.right.find(value)
        else:
            return self.content


class RBNode: #черно красное дерево (узер дерева)
    def __init__(self, val, content=None):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
        self.content = content


class RBTree: #само дерево
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val, content=None):
        new_node = RBNode(val, content)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True 
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node): #метод, который делает дерево черно красным (приводит его к правильному виду)
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent

                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

        self.root.red = False

    def exists(self, val): #поиск элемента
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr.content is None:
            raise Exception('error, node content is None')
        else:
            return curr.content

    def rotate_left(self, x): #вращение влево
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):#вращение вправо
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __repr__(self): #перегрузка оператора вывода
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0): #перегрузка
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        print(node.val, node.content)
        print_tree(node.right, lines, level + 1)


class HashTable: #хеш-таблица
    __collisions = 0

    def __init__(self, n=100):
        self.MAX = n
        self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value): #добавить значение
        hsh = self.__get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hsh]):
            if len(element) == 2 and element[0] == key:
                self.arr[hsh][idx] = (key, value)
                found = True
                break
        if not found and len(self.arr[hsh]) > 0:
            self.arr[hsh].append((key, value))
            self.__collisions += 1
        elif not found:
            self.arr[hsh].append((key, value))

    def __getitem__(self, key): #получить значение
        hsh = self.__get_hash(key)
        for element in self.arr[hsh]:
            if element[0] == key:
                return element[1]

        raise Exception(f"No {key} key in HashTable")

    def __delitem__(self, key): #удалить значение
        hsh = self.__get_hash(key)
        for idx, element in enumerate(self.arr[hsh]):
            if element[0] == key:
                del self.arr[hsh][idx]

    def get_collisions_number(self): #получить кол-во коллизий
        print('Количество коллизий: ',self.__collisions)

    def pr(self): #вывод таблицы
        for i in self.arr:
            print(i)


# file = codecs.open('football_dataset.csv', 'r', 'utf_8_sig')
file = codecs.open('football_dataset_25000.csv', 'r', 'utf_8_sig')
next(file)
row_counter = sum(1 for row in file)
file.seek(0)
next(file)
tree_1 = TreeNode()
rb_tree_1 = RBTree()
table_1 = HashTable(row_counter)
d = dict()
for row in file:
    r = row.split(",")
    w = Command(r[0], r[1], r[2], int(r[3]), r[4], int(r[5]))
    tree_1.insert(value=r[0], content=w)
    rb_tree_1.insert(val=r[0], content=w)
    table_1[r[0]] = w
    d[r[0]] = w


start = time.time()
tree_1.find('Россия').tmp()
end = time.time()
print('Бинарное дерево: ',end-start)

start = time.time()
rb_tree_1.exists('Россия').tmp()
end = time.time()
print('Черно-красное дерево: ',end-start)

start = time.time()
table_1['Россия'].tmp()
end = time.time()
print('Хеш-таблица',end-start)


start = time.time()
d["Россия"].tmp()
end = time.time()
print('Miltimap: ',end-start)



table_1.get_collisions_number()

#table_1.pr()