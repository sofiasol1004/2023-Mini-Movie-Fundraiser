# functions go here



# main routine goes here
while True:
	want_instructions = input("Do you want to read instructions?") .lower()

	if want_instructions == "yes" or want_instructions == "y":
		print("instructions go here")
	elif want_instructions == "no" or want_instructions == "n":
		pass
	else:
		print("please answer yes / no")

print("we are done")