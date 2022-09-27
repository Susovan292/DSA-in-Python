class Stack:
    def __init__(self, max_len: int):
        assert max_len >= 0, "max_length can't be zero"
        self.__stack = []
        self.max_len = max_len
    
    def __is_empty(self):
        if len(self.__stack) <= 0:
            print("\t\t\t\tStack is Empty -- > UNDERFLOW occurred")
            return True
        else:
            return False

    def __is_full(self):
        if len(self.__stack) >= self.max_len:
            print("\t\t\t\tStack is Full -- > OVERFLOW occurred")
            return True
        else:
            return False

    def push(self, value):
        if not self.__is_full():
            self.__stack.append(value)
            return f"{value} pushed to the stack"
        else:
            return None

    def pop(self):
        if not self.__is_empty():
            value = self.__stack.pop()
            print(f"{value} popped from the stack")
            return value

    def peek(self):
        if not self.__is_empty():
            return self.__stack[-1]

    def display_all(self):
        if not self.__is_empty():
            for index in range(len(self.__stack)-1, -1, -1):
                print(self.__stack[index])

def main():
    max_ = int(input("Set max space for the stack : "))
    a = Stack(max_len=max_)

    while True:

        print("Welcome to stack implementation ")
        print("""
                1). Push
                2). POP
                3). Peek
                4). Display All
        """)
        choice = int(input("Enter your choice : "))
        if choice == 1:
            while True:
                v = input("Enter your value to push: ")
                msg = a.push(int(v))
                if msg is None:
                    break
                print(msg)
                choice = input("Do you want to continue pushing (y/n) : ")
                if choice == 'n':
                    break

        elif choice == 2:
            print(a.pop())
        elif choice == 3:
            print(a.peek())
        elif choice == 4:
            a.display_all()


if __name__ == '__main__':
    main()