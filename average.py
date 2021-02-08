# Calculate the average of elements in a given list

def average(given_list):

	if not isinstance(given_list, list):
		return None

	length = len(given_list)

	if length <= 0:
		return 0
	else:
		listSum = sum(given_list)
		listAvg = listSum / float(length)

		return round(listAvg,5)

average([-.5,-.5])
