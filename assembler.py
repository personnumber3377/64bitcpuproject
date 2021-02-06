assemblyfile = str(input("Enter filename for assembly file: "))

assemblystring = open(assemblyfile, "r")

outputfilenamelower = str(input("Enter filename for lower part of output program: "))
outputfilenamehigher = str(input("Enter filename for higher part of output program: "))
lines = assemblystring.readlines()
instructions = ["nop", "mov a, $x", "jump $x", "jumpifz $x", "sub a, x", "add a, x", "test a, x", "jumpifleoreq $x", "mov $x, a", "jumpifle $x", "mov b, $x", "sub b, x", "add b, x", "test b, x", "mov $x, b", "add a, b", "ret", "call $x", "push rbp", "mov rsp, rbp", "pop rbp"]
address = 0
outputfilelower = open(outputfilenamelower, "w+")
outputfilehigher = open(outputfilenamehigher, "w+")
outputfilelower.write("v2.0 raw\n")
outputfilehigher.write("v2.0 raw\n")
for line in lines:
	#line = list(line)
	#print(str(address)+": "+str(line.rstrip()))
	#print(address)
	if "0x" in line:
		index = line.find("0x")
		index2 = 0
		homma = "placeholdervalue"
		while homma != " ":
			index2 = index2 + 1
			try:
				homma = line[index+index2]
			except:
				homma = " "

		number = line[index:index+index2-1]
		#print(str(number)+"2e21")

		line = line.replace(str(number), "x")
		#print(line)
		line = line.rstrip()
		#print("homo")
		if line not in instructions:
			print("invalid instruction at address: "+str(address))
			continue
		indexi = instructions.index(line)
		print(indexi)
		outputfilelower.write(hex(int(indexi))[2:]+ " ")
		if address % 8 == 0:
			outputfilelower.write("\n")

		outputfilehigher.write(hex(int(number, 16))[2:]+ " ")
		if address % 8 == 0:
			outputfilehigher.write("\n")

		address = address + 1
		#print(address)
	else:
		line = line.rstrip()
		indexi = instructions.index(line)
		print(indexi)
		outputfilelower.write(hex(int(indexi))[2:] + " ")
		if address % 8 == 0:
			outputfilelower.write("\n")

		outputfilehigher.write(hex(int(number, 16))[2:]+ " ")
		if address % 8 == 0:
			outputfilehigher.write("\n")

		address = address + 1