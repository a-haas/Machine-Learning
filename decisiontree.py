"""
ftp://public.dhe.ibm.com/software/analytics/spss/support/Stats/Docs/Statistics/Algorithms/13.0/TREE-CART.pdf
http://edoc.hu-berlin.de/master/timofeev-roman-2004-12-20/PDF/timofeev.pdf
http://people.revoledu.com/kardi/tutorial/DecisionTree/how-to-measure-impurity.htm
https://en.wikipedia.org/wiki/Decision_tree_learning
"""

# start root training computation
def begintraining(input, output):
	root = DecisionTree(input, output)
	nodetraining(root)
	return root

# node is from DecisionTree class
def nodetraining(node):
	# if doesn't have output stop and return null
	if len(node.output) <= 0:
		return None
	# if pure algorithm is done
	if node.ispure():
		node.classification = node.output[0][0]
		return node
	# split node dataset
	split = splitchoice(node.input, node.output)
	# save split informations
	node.split = split
	splitdata = splitting(node.input, node.output, split)
	# generate childs
	left = DecisionTree(splitdata["left"][0], splitdata["left"][1])
	right = DecisionTree(splitdata["right"][0], splitdata["right"][1])
	# train each node + append
	if  len(left.output) > 0:
		nodetraining(left)
		node.left = left
	if len(right.output) > 0:
		nodetraining(right)
		node.right = right
	return node

#gini impurity function computation
def giniimpurity(classification):
	# pour chaque classe faire
	# 	proportion classe dans le dataset * (1 - la proportion)
	# fin pour

	classcounter = {}
	for array in classification:
		for classname in array:
			if classname not in classcounter:
				classcounter[classname] = 0
			classcounter[classname] += 1

	total = len(classification)
	gini = 0
	for classname in classcounter:
		proportion = classcounter[classname]/total
		gini += proportion * (1-proportion)
	return gini

# gini delta fonction
def ginidelta(left, right, parent):
	# i(t) = gini impurity
	# lt = left tree / rt = right tree
	# probability of a child tree : len(child)/len(parent)
	# calcul : di(t) = i(t) - p(lt)*i(lt) - p(rt)*i(rt)
	leftbalance = len(left)*giniimpurity(left)
	rightbalance = len(right)*giniimpurity(right)
	total = len(parent)
	return giniimpurity(parent) - leftbalance/total - rightbalance/total

# compute the more appropriate split in the dataset
def splitchoice(dataset, output):
	#init
	# only for value assigning purpose
	maxsplitdelta = 0
	chosensplit = 0
	splitcol = 0
	# unzip by attributes
	byattributes = list(zip(*dataset))
	for col in range(len(byattributes)):
		# tri des valeurs uniques de la colonne en question
		attributeset = sorted(set(byattributes[col]))
		splits = []
		# on énumère toutes les scissions possibles
		for i in range(len(attributeset)-1):
			splits.append((attributeset[i]+attributeset[i+1])/2)
		
		# pour chaque scission on calcule le delta créé
		for split in splits:
			left = []
			right = []
			for i in range(len(byattributes[col])):
				if byattributes[col][i] < split:
					left.append(output[i])
				else:
					right.append(output[i])
			tmpsplitdelta = ginidelta(left, right, output)
			if tmpsplitdelta > maxsplitdelta:
				maxsplitdelta = tmpsplitdelta
				chosensplit = split
				splitcol = col
	return [splitcol, chosensplit]

# split the dataset in function of the split arg
def splitting(dataset, output, split):
	leftinput = []
	leftoutput = []
	rightinput = []
	rightoutput = []
	for i in range(len(dataset)):
		# inferior or equal => left child tree
		if dataset[i][split[0]] <= split[1]:
			leftinput.append(dataset[i])
			leftoutput.append(output[i])
		# else go to the right child tree
		else:
			rightinput.append(dataset[i])
			rightoutput.append(output[i])
	# dictionnary (for convenience) of generated input/output
	return {"left": [leftinput, leftoutput], "right": [rightinput, rightoutput]}

# classifier for only one input
def prediction(input, decisiontree):
	if decisiontree.split is not None:
		splitcol = decisiontree.split[0]
		splitvalue = decisiontree.split[1]
		if input[splitcol] <= splitvalue:
			return prediction(input, decisiontree.left)
		else:
			return prediction(input, decisiontree.right)
	else:
		return decisiontree.classification

# classifier for a testing dataset
def datasetprediction(dataset, decisiontree):
	predictions = []
	for input in dataset:
		predictions.append(prediction(input, decisiontree))
	return predictions

class DecisionTree():
	def __init__(self, input, output):
		self.left = None
		self.right = None
		self.split = None
		self.classification = ""
		self.input = input
		self.output = output

	# return True if all the outputs are from the same class
	def ispure(self):
		classname = self.output[0][0]
		for array in self.output:
			for current in array:
				if current != classname:
					return False
		return True

	# output the decision tree in the console
	def representation(self, header, depth=0):
		# escape one line
		print("")
		# start rendering
		if self.split is not None:
			msg = "Condition : " + header[self.split[0]] + " <= " + str(self.split[1])
			print("\t"*depth + msg)
			# left side
			if self.left is not None:
				self.left.representation(header, depth+1)
			# right side
			if self.right is not None:
				self.right.representation(header, depth+1)
		else:
			print("\t"*depth + "Classification : " + self.classification)