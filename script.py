filename = str(input("Enter filename to open (lower): "))
filename2 = str(input("Enter filename to open (higher): "))
addresses = str(input("address before instruction? (yes/NO): ")) == "yes"
file1 = open(filename, "r")
file2 = open(filename2, "r")

datahigher = file2.read()
datahigher = datahigher.replace("\n", " ")
datahigher = datahigher.split(" ")
datahigher = datahigher[2:-1]

datalower = file1.read()
datalower = datalower.replace("\n", " ")
datalower = datalower.split(" ")
datalower = datalower[2:-1]

print(datalower)

instructions = ["nop", "mov a, $x", "jump $x", "jumpifz $x", "sub a, x", "add a, x", "test a, x", "jumpifleoreq $x", "mov $x, a", "jumpifle $x", "mov b, $x", "sub b, x", "add b, x", "test b, x", "mov $x, b", "add a, b", "ret"]
address = 0
for element in datalower:

	stringtobeprinted = instructions[int(element, 16)]
	stringtobeprinted = stringtobeprinted.replace("x", ("0x"+str(datahigher[address])))
	if addresses:
		print(str(hex(address)) + ": " + stringtobeprinted)
	else:
		print(stringtobeprinted)
	address = address + 1

file1.close()
