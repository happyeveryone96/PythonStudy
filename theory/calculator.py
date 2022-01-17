def plus(a, b):
  if (type(a) is (int or float)) and (type(b) is (int or float)):
    return a + b
  else:
    return None

def minus(a, b):
  if (type(a) is (int or float)) and (type(b) is (int or float)):
    return a - b
  else:
    return None

def times(a, b):
  if (type(a) is (int or float)) and (type(b) is (int or float)):
    return a * b
  else:
    return None

def division(a, b):
  if (type(a) is (int or float)) and (type(b) is (int or float)):
    return a / b
  else:
    return None

def negation(a):
  if type(a) is (int or float)):
    return -a
  else:
    return None

def power(a, b):
  if (type(b) is (int or float)) and (type(a) is (int or float)):
    return pow(a, b)
  else:
    return None

def remainder(a, b):
  if (type(a) is (int or float)) and (type(b) is (int or float)):
    return a % b
  else:
    return None
