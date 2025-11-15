source = "source.txt"
destination = "oddlines.txt"

f1 = open(source, "r")
f2 = open(destination, "w")

lines = f1.readlines()  

for i in range(len(lines)):
    if i % 2 == 0:      
        f2.write(lines[i])

f1.close()
f2.close()

print("Odd-numbered lines copied successfully!")
