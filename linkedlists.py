import copy


class List:
    class Node:
        def __init__(self, val, next=None, prev=None) -> None:
            self.val = val
            self.next: None | List.Node = next
            self.prev: None | List.Node = prev

        def find_index(self, depth):
            if depth == 0:
                return self
            if self.next:
                return self.next.find_index(depth - 1)
            raise IndexError

        def find_value(self, val):
            if self.val == val:
                return self
            if self.next:
                return self.next.find_value(val)

        def find_id(self, val):
            if self.val.id == val:
                return self
            if self.next:
                return self.next.find_id(val)

        def find_type(self, val, count=0):
            if self.val.type == val:
                count += 1
            if self.next:
                count = self.next.find_type(val, count)
            return count

        def find_end(self):
            if self.next:
                return self.next.find_end()
            return self

        def print_list(self):
            print(self.val)
            if self.next:
                self.next.print_list()

        def print_back(self):
            print(self.val)
            if self.prev:
                self.prev.print_back()

        def print_self(self):
            if self.val.type == "locomotive":
                print(
                    f"Train of type locomotive has ID: {self.val.id}, a full status of {self.val.isFull}, a horn frequency of {self.val.horn_frequency}, and a horn duration of {self.val.horn_duration}."
                )
            else:
                print(
                    f"Train of type {self.val.type} has ID: {self.val.id}, and a full status of {self.val.isFull}."
                )

        def print_extra(self):
            self.print_self()
            if self.next:
                self.next.print_extra()

        def move_through_backwards(self):
            pass

    def __init__(self, val=None) -> None:
        self.root: List.Node = List.Node(val)
        self.len = 1

    def insert_front(self, val):
        old_root = self.root
        new_root = List.Node(val, old_root)
        old_root.prev = new_root
        self.root = new_root
        self.len += 1

    def insert(self, index, val):
        if index >= self.len:
            self.append(val)
            return
        if abs(index) >= self.len or index == 0:
            old_root = self.root
            new_root = List.Node(val, old_root)
            old_root.prev = new_root
            self.root = new_root
            self.len += 1
            return
        old_node = self.get_index(index)
        prev = old_node.prev
        new_node = List.Node(val, old_node, prev)
        prev.next = new_node
        old_node.prev = new_node
        self.len += 1

    def pop(self, index=None):
        if index is None:
            self.get_index(self.len - 2).next = None
            return
        if index == 0:
            self.root = self.root.next
            self.root.prev = None
        else:
            current = self.get_index(index)
            prev = current.prev
            next = current.next
            if next:
                next.prev = prev
            if prev:
                prev.next = next
        self.len -= 1

    def append(self, val):
        end = self.root.find_end()
        end.next = List.Node(val, None, end)
        self.len += 1

    def remove(self, val):
        if self.root.val == val:
            self.root = self.root.next
            self.root.prev = None
            return
        if found := self.root.find_value(val):
            prev = found.prev
            next = found.next
            if next:
                next.prev = prev
            prev.next = next
            return
        raise IndexError

    def find(self, key: str, val):
        if key == "id":
            return self.root.find_id(val)
        if key == "type":
            return self.root.find_type(val)

    def print_list(self, *, backwards=False):
        if backwards:
            self.root.find_end().print_back()
        else:
            self.root.print_list()

    def print_index(self, index):
        print(self.get_index(index).val)

    def get_index(self, index):
        return self.root.find_index(index)

    def print_extra(self):
        self.root.print_extra()

    def reverse(self):
        old_node = copy.copy(self.root)
        new_list = List(old_node.find_index(self.len - 1).val)
        for i in range(self.len - 2, -1, -1):
            new_list.append(old_node.find_index(i).val)
        self.root = new_list.root

    def fullswap(self):
        for i in range(0, self.len, 2):
            if i + 1 < self.len:
                self.swap_nodes(self.get_index(i), self.get_index(i + 1))

    def swap_nodes(self, node1: Node, node2: Node):
        p1 = node1.prev
        n2 = node2.next

        node2.prev = p1
        node2.next = node1
        node1.prev = node2
        node1.next = n2
        if p1:
            p1.next = node2
        else:
            self.root = node2
        if n2:
            n2.prev = node1
