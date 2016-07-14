import math
#custom imports
import usefulfunctions

"""
Tutorial used :
http://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
"""

"""
Separate attributes and create useful stats
"""

def separatebyclass(input, output):
	res = {}
	for i in range(len(input)):
		classname = output[i][0]
		if(classname not in res):
			res[classname] = []
		res[classname].append(input[i])
	return res

def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def standarddeviation(numbers):
	avg = mean(numbers)
	#formule d'une série statistique
	variance = 0
	for x in numbers:
		variance += pow(x-avg,2)
	variance = variance/float(len(numbers)-1)
	return math.sqrt(variance)

def computestats(dataset):
	stats = []
	for attribute in zip(*dataset):
		stats.append([mean(attribute), standarddeviation(attribute)])
	return stats

def computestatsbyclass(dataset, output):
	separated = separatebyclass(dataset, output)
	statsbyclass = {}
	for classname, classattributes in separated.items():
		statsbyclass[classname] = computestats(classattributes)
	return statsbyclass

# get the probabilities of a certain class to be chose
def computeclassprobabilities(output):
	res = {}
	for value in output:
		#the output is a matrix
		classname = value[0]
		if (classname not in res):
			res[classname] = 1
		res[classname]+=1
	outputlen = len(output)
	for classname, probability in res.items():
		res[classname] /= outputlen 
	return res
"""
Do the probabilities
"""

"""
v : value
m : mean
sd : standard deviation
"""
def gaussianprobability(v, m, sd):
	variance = math.pow(sd,2)
	exponent = - math.pow((v - m),2)/(2*variance)
	denominator = math.sqrt(2*math.pi*variance)
	return (1/denominator)*math.exp(exponent)

"""
return the input vector probability for each class
"""
def computeprobabilities(stats, input, classprobabilities):
	probabilities = {}
	# do probabilities on each class
	for classname, classstats in stats.items():
		probabilities[classname] = classprobabilities[classname]
		# do probabilities on each class' attribute
		for i in range(len(classstats)):
			"""
			v : value
			m : mean
			sd : standard deviation
			"""
			m, sd = classstats[i]
			v = input[i]
			# multiply each probabilities (naive bayes)
			probabilities[classname] *= gaussianprobability(v, m, sd)
	return probabilities

def prediction(probabilities):
	#max value in dictionnary
	return usefulfunctions.keywithmaxvalue(probabilities)

def inputprediction(stats, inputvector, classprobabilities):
	#probabilities
	probabilities = computeprobabilities(stats, inputvector, classprobabilities)
	#prediction
	return prediction(probabilities)

#might wanna add some class probabilities computation
def traindataset(dataset, output):
	stats = computestatsbyclass(dataset, output)
	classprobabilities = computeclassprobabilities(output)
	return [stats, classprobabilities]

def datasetprediction(dataset, training):
	predictions = []
	for vector in dataset:
		predictions.append(inputprediction(training[0], vector, training[1]))
	return predictions