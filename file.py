f = open("demo.txt", "r")
data = f.read()

print(data)
print(type(data))
f.close()

with open("demo.txt", "w")as f:
  f.write("hey")


