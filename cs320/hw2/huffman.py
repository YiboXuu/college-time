import sys


frequenciesList = []
fList = {}
n=0
def file_character_frequencies(file_name):
	wordList = []
	letterFrequency = {}
	file = open(file_name, 'rU')
	for line in file:
		for word in line:
		   wordList.append(word);
	#print(format(wordList))

	for word in wordList:
		for letter in word:
			keys = letterFrequency.keys()
			if letter in keys:
				letterFrequency[letter] += 1
			else:
				letterFrequency[letter] = 1
	#print(format(letterFrequency))
	return letterFrequency


class PriorityTuple(tuple):
    """A specialization of tuple that compares only its first item when sorting.
    Create one like this: PriorityTuple((x, y, z)) # note the doubled parens"""
    def __lt__(self, other):
        return self[0] < other[0]

    def __le__(self, other):
        return self[0] <= other[0]


def huffman_codes_from_frequencies(fre):
    if (len(fre) == 2):
        return dict(zip(fre.keys(), ['0', '1']))

    for key, value in fre.items():
        frequenciesList.append((value, key))

    buildHeap(frequenciesList)

    for currentValue in range(len(frequenciesList) - 1):
        t1 = heapExtractMin(frequenciesList)
        t2 = heapExtractMin(frequenciesList)
        mergedt = PriorityTuple((t1[0]+t2[0], t1, t2))
        heapInsert(frequenciesList, mergedt)
    s = ""
    Addmethod(frequenciesList[0], s)

    return fList

def Addmethod(t, s):
    global fList
    if(len(t) == 2):
        fList[t[1]] = s
    else:
        Addmethod(t[1], s + '1')
        Addmethod(t[2], s + '0')

def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)
    #return {}


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def parent(i):
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return left(i) + 1

def heapify(A, i, n=None):
    if n is None:
        n = len(A)
    if not(i < n):
        return

    l = left(i)
    r = right(i)
    smallest = i
    if l < n and A[l][0] < A[smallest][0]:
        smallest = l
    if r < n and A[r][0] < A[smallest][0]:
        smallest = r
    if smallest != i:
        swap(A,i,smallest)
        heapify(A, smallest, n)

def buildHeap(A):
    n = len(A)
    for i in range(int(n / 2), -1, -1):
        heapify(A, i, n)


def heapExtractMin(A):
    min = A[0]
    swap(A, 0, len(A) - 1)
    A.pop(len(A) - 1)
    heapify(A, 0, len(A))
    return min

def heapInsert(A, v):
    if len(A) == 0:
        A.append(v)
    else:
        A.append(v)
        start = len(A) - 1
        while start > 0 and A[parent(start)][0] > A[start][0]:
            x = A[start]
            swap(A, start, parent(start))
            start = parent(start)





def main():
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    codes = huffman_codes_from_frequencies(frequencies)
    encode_file_using_codes(sys.argv[1],codes)
    decode_file_using_codes(sys.argv[1]+"_encoded",codes)


if __name__ == '__main__':
    main()