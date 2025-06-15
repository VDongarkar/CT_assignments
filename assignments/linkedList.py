class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else " -> None\n")
            current = current.next
    
    def delete_nth(self, n):
        try:
            
            if not self.head:
                raise IndexError("Cannot delete from empty list")
            
            if n < 1:
                raise IndexError("Index must be 1 or greater")
            
            
            if n == 1:
                self.head = self.head.next
                return
            
    
            current = self.head
            for i in range(1, n - 1):
                if not current.next:
                    raise IndexError("Index out of range")
                current = current.next
            

            if not current.next:
                raise IndexError("Index out of range")

            current.next = current.next.next
            
        except IndexError as e:
            print(f"Error: {e}")

if __name__ == "__main__":

    ll = LinkedList()
    
    print("=== Testing Singly Linked List ===\n")
    

    print("1. Adding elements: 10, 20, 30, 40")
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)
    ll.print_list()
    
    print("\n2. Deleting 2nd node (20)")
    ll.delete_nth(2)
    ll.print_list()
    
    print("\n3. Deleting 1st node (10)")
    ll.delete_nth(1)
    ll.print_list()
    

    print("\n4. Deleting 2nd node (40)")
    ll.delete_nth(2)
    ll.print_list()
    
    print("\n5. Testing exception handling:")
    ll.delete_nth(1) 
    print("After deleting last node:")
    ll.print_list()
    
    print("\nTrying to delete from empty list:")
    ll.delete_nth(1)
    

    ll.add(100)
    ll.add(200)
    print("\nCurrent list:")
    ll.print_list()
    
    print("\nTrying to delete 5th node (out of range):")
    ll.delete_nth(5)
    
    print("\nTrying to delete 0th node (invalid index):")
    ll.delete_nth(0)