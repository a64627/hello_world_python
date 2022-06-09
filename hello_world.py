def hello():
    return 'Hello World!'

def print_hello():
    print(hello())
    
def name():
    name = input("Enter your name: ")
    print("Hello", name + "!")
    
print_hello()
name()