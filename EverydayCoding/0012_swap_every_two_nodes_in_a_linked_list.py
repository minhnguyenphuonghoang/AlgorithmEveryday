from BenchmarkUtil import benchmark_util
"""In a given array of numbers, one element will show up once and the others will each show up twice.
Can you find the number that only appears once in O(n) linear time?
Bonus points if you can do it in O(1) space as well.
"""
NO_OF_SOLUTION = 3


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def get_size(self):
        count = 0
        pointer = self.head
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

    def add(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = new_node

    def remove(self, index):
        pass

    def find(self, value):
        pointer = self.head
        while pointer is not None:
            if pointer.value == value:
                return True
            pointer = pointer.next
        return False

    def to_string(self):
        final_string = "HEAD: "
        pointer = self.head
        while pointer is not None:
            final_string += "{} -> ".format(pointer.value)
            pointer = pointer.next
        return final_string + "None"

    def clone(self):
        cloned = LinkedList()
        pointer = self.head
        while pointer is not None:
            cloned.add(Node(pointer.value))
            pointer = pointer.next
        return cloned


linked_list = LinkedList(Node(1))
linked_list.head.next = Node(2)
linked_list.head.next.next = Node(3)
linked_list.head.next.next.next = Node(4)

print("Size of the list before adding {}".format(linked_list.get_size()))
print(linked_list.to_string())
print("Find value 5 in linked list, result {}".format(linked_list.find(5)))
linked_list.add(Node(5))
print("Size of the list after adding {}".format(linked_list.get_size()))
print(linked_list.to_string())
print("Find value 5 in linked list, result {}".format(linked_list.find(5)))


def solution_01(ls):
    ls1 = ls.clone()
    idx = 1
    pointer = ls1.head
    while pointer is not None:
        if idx == 1 and pointer.next is not None:
            temp = pointer.value
            pointer.value = pointer.next.value
            pointer.next.value = temp
            idx = 2
        else:
            idx = 1
        pointer = pointer.next
    return ls1


def solution_02(ls):
    ls1 = ls.clone()
    pointer = ls1.head
    for idx in range(ls1.get_size()):
        if pointer is None or pointer.next is None:
            break
        if idx % 2 == 0:
            temp = pointer.value
            pointer.value = pointer.next.value
            pointer.next.value = temp
        pointer = pointer.next
    return ls1


def solution_03(ls):
    ls1 = ls.clone()
    pointer = ls1.head
    idx = 0
    while pointer is not None and pointer.next is not None:
        if pointer is None or pointer.next is None:
            break
        if idx % 2 == 0:
            temp = pointer.value
            pointer.value = pointer.next.value
            pointer.next.value = temp
        pointer = pointer.next
        idx += 1
    return ls1


expected_result = solution_01(linked_list)
tests = [linked_list]
results = [expected_result]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result.to_string() == results[i].to_string(), \
            "Solution {} had wrong result '{}' - expecting '{}'".format("solution_0{}".format(sln_idx),
                                                                        result, results[i])

