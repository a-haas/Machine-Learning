import decisiontree
import datahandler

def main():
	#load csvs
	input = datahandler.csvtolist("datasets/iris/iris-input.csv")
	output = datahandler.csvtolist("datasets/iris/iris-output.csv")
	header = datahandler.csvtoheader("datasets/iris/iris-header.csv")
	#float csv problem
	input = datahandler.tofloat(input)
	#start training decision tree
	maxtree = decisiontree.begintraining(input, output)
	maxtree.representation(header)
	# predictions
	res = decisiontree.datasetprediction(input, maxtree)
	
if __name__ == '__main__':
	main()