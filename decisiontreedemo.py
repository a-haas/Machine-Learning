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
	maxtree.representation(header)
	# predictions
	# load testing csvs
	testinginput = datahandler.csvtolist("datasets/iris/testing-iris-input.csv")
	testingoutput = datahandler.csvtolist("datasets/iris/testing-iris-output.csv")
	#float csv problem
	testinginput = datahandler.tofloat(testinginput)
	res = decisiontree.datasetprediction(testinginput, maxtree)
	print(res)
	
if __name__ == '__main__':
	main()