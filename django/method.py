class Car():
  
  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")

  def __str__(self):
    return f"Car with {self.wheels} wheels"

  def start(self):
    print(self.color)
    print("I started")

# porche = Car()

porche = Car(color="green", price="$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)

# porche.color = "Red Sexy Red"
# porche.start()