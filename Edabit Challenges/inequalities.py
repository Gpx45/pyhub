
def correct_signs(string):
	eval(string)
	if string:
		print("True")
		return True
	else:
		print("False")
		return False

correct_signs("1 < 2")