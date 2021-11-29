## Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    carry = 0
    dummy = ListNode()
    list = []
    while l1 != None or l2 != None:

        l1 = ListNode(0, None) if l1 == None else l1
        l2 = ListNode(0, None) if l2 == None else l2

        sum = l1.val + l2.val + carry
        carry = sum // 10
        digit = sum % 10
        list.append(digit)
        l1 = l1.next
        l2 = l2.next

    if sum > 9:
        sum = sum // 10
        list.append(sum)

    last_item = len(list) - 1
    while last_item >= 0:
        dummy = ListNode(list[last_item], dummy)
        last_item = last_item - 1

    return {"linkedlist": dummy, "list": list}


first_num = ListNode(3, None)
second_num = ListNode(4, first_num)
l1 = ListNode(2, second_num)

a = ListNode(4, None)
b = ListNode(6, a)
l2 = ListNode(5, b)

# l1 = ListNode(0, None)
# l2 = ListNode(0, None)

# a = ListNode(9, None)
# b = ListNode(9, a)
# c = ListNode(9, b)
# d = ListNode(9, c)
# e = ListNode(9, d)
# f = ListNode(9, e)
# l1 = ListNode(9, f)


# x = ListNode(9, None)
# y = ListNode(9, x)
# z = ListNode(9, y)
# l2 = ListNode(9, z)


result = addTwoNumbers(l1, l2)
print(result["list"])
# while result.next != None:
#     print(result.val)
#     result = result.next
# print(result.next.val)
# print(result.next.next.val)
