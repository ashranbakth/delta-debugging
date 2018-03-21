import sys
import subprocess


def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

def split_list(a_list):
    half = len(a_list)/2
    return a_list[:int(half)], a_list[int(half):]


def getBashCommand(Set):
	""" return the command from the terminal """
	command = ""
	for x in range(2,len(sys.argv)):
		if(x == 2):
			command = command + sys.argv[x]
		else:
			command = command + " " + sys.argv[x]

	for x in Set:
		command = command + " " + str(x)
	return command


def DeltaDebugging(result_set, Set):
	""" returns a list that is interesting """
	if(len(Set) == 1):
		return Set
	P1, P2 = split_list(Set)
	if(subprocess.call(getBashCommand(union(result_set,P1)), shell=True)):
		return DeltaDebugging(result_set, P1)
	if(subprocess.call(getBashCommand(union(result_set,P2)), shell=True)):
		return DeltaDebugging(result_set, P2)
	else:
		return union(DeltaDebugging(union(result_set,P2), P1),
			DeltaDebugging(union(result_set,P1),P2))

def main():
	size_of_set = int(sys.argv[1])

	Set = []
	for x in range(0, size_of_set):
		Set.append(x)

	result_set = []
	result_set = DeltaDebugging(result_set,Set)
	print(sorted(result_set))

	
	
	

if __name__ == '__main__':
	main()