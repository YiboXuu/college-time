import sys

# provided
def read_array(filename):
    in_list = []
    with open(filename, 'r+') as input_file:
        for line in input_file:
            in_list.append(int(line))
    return in_list


# implement
def count_inversions(in_list):
	if (len(in_list) <= 1):
		return 0
	
	mid = (len(in_list)//2)
		
	former = in_list[:mid]
	latter = in_list[mid:]
	left = count_inversions(former)
	right = count_inversions(latter)
	merged = merge_i(former, latter,in_list)
	
	inversions = left + right + merged
	return inversions

# implement
def merge_i(l_list, r_list,in_list):
	leftIndex = 0
	rightIndex = 0
	inversions = 0
	k=0
	print(in_list)
	while (leftIndex < len(l_list) and rightIndex < len(r_list)):
		if l_list[leftIndex] <= r_list[rightIndex]:
			in_list[k] = l_list[leftIndex]
			leftIndex += 1
		else:
			in_list[k]= r_list[rightIndex]
			rightIndex += 1
			inversions = inversions +  (len(l_list)-leftIndex)
		k=k+1	
		
	while (leftIndex<len(l_list)):
			in_list[k] = l_list[leftIndex]
			leftIndex = leftIndex+1
			k = k+1
	while (rightIndex<len(r_list)):
			in_list[k] = r_list[rightIndex]
			rightIndex = rightIndex+1
			k = k+1	
	print(in_list)

	return inversions

# provided
if __name__ == '__main__':
    filename = sys.argv[1]
    in_list = read_array(filename)
    print(count_inversions(in_list))