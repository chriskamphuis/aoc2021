from math import ceil, floor

lines = [eval(l) for l in open('input.txt')]

class Node:
    def __init__(self, n1, n2, parent=None):
        if not type(n1)==list: self.l = n1
        else: self.l = Node(n1[0], n1[1], self)
        if not type(n2)==list: self.r = n2
        else: self.r = Node(n2[0], n2[1], self)
        self.parent = parent

    __str__ = lambda self: f'[{str(self.l)}, {str(self.r)}]'

    def reduce(self):
        while True:
            if nested := self.find_nested(list()): nested[0].explode()
            elif ge_ten := self.ge_ten(list()): ge_ten[0].split()
            else: break

    is_l_child = lambda self: not (self.parent is None) and self.parent.l is self
    is_r_child = lambda self: not (self.parent is None) and self.parent.r is self
    is_root = lambda self: self.parent is None

    def add(self, node):
        new_root = Node(self, node)
        new_root.l.parent = new_root
        new_root.r.parent = new_root 
        new_root.reduce()
        return new_root

    def explode(self):
        if self.is_l_child(): 
            self.parent.l = 0
            
            n = self.parent.r
            if type(n) == int: self.parent.r += self.r
            else:
                while type(n.l) is not int: n = n.l
                n.l += self.r
            
            n = self.parent
            while n.is_l_child(): n = n.parent
            if n.is_r_child():
                if type(n.parent.l) is int: n.parent.l += self.l
                else:
                    n = n.parent.l
                    while type(n.r) is not int: n = n.r
                    n.r += self.l

        else:
            self.parent.r = 0
            
            n = self.parent.l
            if type(n) == int: self.parent.l += self.l
            else:
                while type(n.r) is not int: n = n.r
                n.r += self.l
            
            n = self.parent
            while n.is_r_child(): n = n.parent
            if n.is_l_child():
                if type(n.parent.r) is int: n.parent.r += self.r
                else:
                    n = n.parent.r
                    while type(n.l) is not int: n = n.l
                    n.l += self.r


    def split(self):
        if type(self.l) == int and self.l >= 10: self.l = Node(floor(self.l/2), ceil(self.l/2), self)
        else: self.r = Node(floor(self.r/2), ceil(self.r/2), self)

    def find_nested(self, nested, depth=4):
        if depth == 0: nested.append(self)
        if type(self.l) == Node and not nested: self.l.find_nested(nested, depth-1)
        if type(self.r) == Node and not nested: self.r.find_nested(nested, depth-1)
        return nested

    def ge_ten(self, ge_ten_list):
        cont = not ge_ten_list
        if cont and type(self.l) is Node: self.l.ge_ten(ge_ten_list)
        if cont and type(self.l) is int and self.l >= 10: ge_ten_list.append(self)
        if cont and type(self.r) is Node: self.r.ge_ten(ge_ten_list)
        if cont and type(self.r) is int and self.r >= 10: ge_ten_list.append(self)
        return ge_ten_list

    def magnitude(self):
        left, right = 0, 0
        if type(self.l) is int: left = self.l * 3
        else: left = self.l.magnitude() * 3
        if type(self.r) is int: right = self.r * 2
        else: right = self.r.magnitude() * 2
        return left + right

maximum = -1
for i, l1 in enumerate(lines):
    for j, l2 in enumerate(lines):
        if i == j: 
            continue
        magnitude = Node(l1[0], l1[1]).add(Node(l2[0], l2[1])).magnitude()
        if magnitude > maximum: maximum = magnitude
print(maximum)
