
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


def init_list():

    global node_A
    global node_E

    node_A = Node('A')
    node_B = Node('B')
    node_D = Node('D')
    node_E = Node('E')

    node_A.next = node_B
    node_B.prev = node_A
    node_B.next = node_D
    node_D.prev = node_B
    node_D.next = node_E
    node_E.prev = node_D


def print_list():

    # global node_A

    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


# myway
def print_reverse_list():

    # global node_E

    node = node_E
    while node:
        print(node.data)
        node = node.prev
    print()


def insert_list(str_data):

    # 왜 여기서 이렇게 global을 선언을 해야만 아래
    # node_E = obj가 효력을 가질까
    global node_E

    global node_A
    node = node_A

    obj = Node(str_data)

    while node:

        # 가장 앞에 node를 입력할 때
        if obj.data < node.data:

            obj.next = node
            node.prev = obj
            node_A = obj
            return

        elif node.next is not None \
                and obj.data < node.next.data:
            obj.next = node.next
            obj.prev = node
            node.next.prev = obj
            node.next = obj
            return

        # 가장 뒤에 node를 입력할 때 (node_E 뒤)
        elif node.next is None:
            node.next = obj
            obj.prev = node

            # 1 more thing !
            # 3_linked_list의 delete_list method에서
            # 배웠던 것
            node_E = obj
            return
        node = node.next


def delete_list(str_data):

    global node_E
    global node_A

    node = node_A

    while node:

        # 가장 처음 node(node_A)를 삭제할 때
        if node.data == str_data:
            # 두 번째 node의 prev를 제거
            node.next.prev = None

            node_A = node.next
            del node
            return

        elif node.next.next is not None \
            and node.next.data == str_data:

            obj = node.next

            node.next.next.prev = node

            node.next = node.next.next
            # 아래 코드가 위 코드보다 뒤에 있어서 아래 코드가 꼬여버림.
            # node.next.next.prev = node

            del obj
            return

        # 가장 마지막 node를 삭제할 때 (node_E 뒤)
        elif node.next.next is None \
                and node.next.data == str_data:

            obj = node.next
            node.next = None
            del obj

            node_E = node

        node = node.next


if __name__ == '__main__':
    init_list()
    # print_list()

    insert_list('C')
    # print_list()
    # print_reverse_list()

    insert_list('G')
    # print_list()
    # print_reverse_list()

    insert_list('F')
    # print_list()
    # print_reverse_list()

    insert_list('H')
    # print_list()
    # print_reverse_list()

    delete_list('A')
    print_list()
    print_reverse_list()

    insert_list('A')
    print_list()
    print_reverse_list()

    insert_list('I')
    print_list()
    print_reverse_list()

    delete_list('I')
    print_list()
    print_reverse_list()

