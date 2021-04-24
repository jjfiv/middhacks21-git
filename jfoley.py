"""
This prints 'yay git tutorial' between two triangles.
"""

def message():
    return "Hooray, Git Tutorial!";

def print_triangle(n, rev=False):
    if rev:
        for i in reversed(range(n)):
            print("." * i)
    else:
        for i in range(n):
            print("." * i)


# Yes, the example file is in Python.
if __name__ == '__main__':
  print_triangle(len(message()))
  print(message())
  print_triangle(len(message()), rev=True)
