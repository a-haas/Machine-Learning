import decisiontree
import datahandler

def main():
	#load training csvs
	traininginput = datahandler.csvtolist("datasets/iris/training-iris-input.csv")
	trainingoutput = datahandler.csvtolist("datasets/iris/training-iris-output.csv")
	header = datahandler.csvtoheader("datasets/iris/iris-header.csv")
	#float csv problem
	traininginput = datahandler.tofloat(traininginput)
	#start training decision tree
	maxtree = decisiontree.begintraining(traininginput, trainingoutput)
	print("Max tree representation :")
	maxtree.representation(header)
	# optimisation parameter => here 10% of the dataset
	nmin = len(trainingoutput)* 0.1
	prunedtree = decisiontree.pruning(maxtree, nmin)
	print("\nPruned tree representation :")
	prunedtree.representation(header)
	# predictions
	# load testing csvs
	testinginput = datahandler.csvtolist("datasets/iris/testing-iris-input.csv")
	testingoutput = datahandler.csvtolist("datasets/iris/testing-iris-output.csv")
	#float csv problem
	testinginput = datahandler.tofloat(testinginput)
	res = decisiontree.datasetprediction(testinginput, prunedtree)
	print("\nGenerated classification results :\n")
	print(res)
	ratio = datahandler.compareoutputs(res, testingoutput)
	print("\nPredictions ratio :\n")
	print(str(ratio) + " %")

if __name__ == '__main__':
	main()