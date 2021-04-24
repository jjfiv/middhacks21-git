"""
This is a python file for you to play with. 

For fun, it is also runnable:
python3 jfoley.py

"""

def hello():
    return "Hello World!";

def print_triangle(n, rev=False):
    if rev:
        for i in reversed(range(n)):
            print("." * i)
    else:
        for i in range(n):
            print("." * i)


# Yes, the example file is in Python.
if __name__ == '__main__':
  print_triangle(len(hello()))
  print(hello())
  print_triangle(len(hello()), rev=True)
