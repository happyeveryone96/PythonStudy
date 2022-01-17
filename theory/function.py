# def say_hello(name="anonymous"):
#   print("hello", name)

# say_hello("Nicolas")
# say_hello()
def say_hello(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hello("nico", 12)
print(hello)

# Keyworded Arguments
hello = say_hello(age=12, name="Nico")
print(hello)

def plus(a, b=0):
  print(a + b)

def minus(a, b=0):
  print(a - b)

plus(2, 5)
minus(2, 5)
minus(2)

def p_plus(a, b):
  print(a + b)

def r_plus(a, b):
  return a + b
  print("asdasdasd")

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)
print(p_result, r_result)