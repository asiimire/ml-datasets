print("Simple program data analysis program")
print()

scan_file={}

with open("myfile.csv","r") as file:
	for data in file.read().split('\n'):
		scan_file.update({data.split(',')[0]:data.split(',')[1:]})

for x,y in scan_file.items():
	print(x, end=" - ")
	print(y)

print("All the contents of myfile.csv has been read into a dictionary")
