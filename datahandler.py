#classic imports
import csv

"""
Working with some CSV reading + formatting stuff

CSV should be in to part
dataset.csv which contains only the data
header.csv which contains only the columns name (used for the dict)
"""
# return an input file into a matrix
def csvtolist (filename):
	with open(filename, 'r') as data:
		return list(csv.reader(data))

def tofloat(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] = float(matrix[i][j])
	return matrix

def csvtoheader(filename):
	#init
	header = []
	with open(filename, 'r') as data:
		reader = csv.reader(data)
		#get 1D header array
		for row in reader:
			header.extend(row)
	return header

#might be useful for runtime 
def csvtoattributearray(filename, headerfilename):
	#init
	attributearray = {}
	#read the files
	dataset = csvtolist(filename)
	header = csvtoheader(headerfilename)
	#add dictionnary attribute
	for attribute in header:
		attributearray[attribute] = []
	#complete the attributes' array
	for row in dataset:
		#index of the row
		for i in range(len(row)):
			attributearray[header[i]].append(row[i])
	return attributearray

def splitio(inputname, outputname, matrix):
	inputfile = open(inputname, 'w', newline='\n')
	inputwriter = csv.writer(inputfile, delimiter=',')
	outputfile = open(outputname, 'w', newline='\n')
	outputwriter = csv.writer(outputfile, delimiter=',')
	for array in matrix:
		#to avoid last column presumed as input 
		#might need a fix for different datasets
		output = []
		output.append(array.pop())
		inputwriter.writerow(array)
		outputwriter.writerow(output)
	inputfile.close()
	outputfile.close()

"""
Normalisation stuff
"""
def matrixmin(matrix):
	currentmin = matrix[0][0]
	for array in matrix:
		value = min(array)
		if value < currentmin:
			currentmin = value
	return float(currentmin)

def matrixmax(matrix):
	currentmax = matrix[0][0]
	for array in matrix:
		value = max(array)
		if value > currentmax:
			currentmax = value
	return float(currentmax)

#normalisation of a matrix with float or integer values only
def normalise(matrix, max, min):
	normalisedmatrix = []
	for array in matrix:
		normalisedarray = []
		for data in array:
			normalisedarray.append(normaliseformula(data, max, min))
		normalisedmatrix.append(normalisedarray)
	return normalisedmatrix

#range [0;1]
def normaliseformula(data, max, min):
	#convert to float
	data = float(data)
	return (data - min)/(max - min)	

# comparison
# correct is a matrix (because it is how csv create it)
# generated is an array (this is the way the classifier returns the data)
def compareoutputs(generated, correct):
	rate = 0
	for i in range(len(generated)):
		if generated[i] == correct[i][0]:
			rate += 1
	return rate/len(generated)*100