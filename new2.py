myUniqueList = []
myLeftOvers = []


def fun(a):
	if a not in myUniqueList:
		myUniqueList.append(a)
		return True
	else:
		myLeftOvers.append(a)
		return False

fun(1)
fun(2)
fun(3)
fun(4)
fun("Bertie")
fun(4)
fun("b")
fun("Bertie")

print(myUniqueList)
print(myLeftOvers)
