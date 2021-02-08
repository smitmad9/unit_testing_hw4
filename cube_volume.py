# Calculate the volume of a cube given a side length

def volume(length):

	if length <= 0:
		print("Length must be greater than 0 to have volume.")
		return 0
	else:
		return (length * length * length)
