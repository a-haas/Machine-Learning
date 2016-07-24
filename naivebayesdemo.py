#module imports

#my module imports
import datahandler
import naivebayes

def main():
	# TRAINING
	# read training csvs
	traininginput = datahandler.csvtolist("datasets/iris/training-iris-input.csv")
	trainingoutput = datahandler.csvtolist("datasets/iris/training-iris-output.csv")
	# float problem
	traininginput = datahandler.tofloat(traininginput)
	# normalisation
	min = datahandler.matrixmin(traininginput)
	max = datahandler.matrixmax(traininginput)
	traininginput = datahandler.normalise(traininginput, max, min)
	# naive bayes classification
	# train with the dataset
	training = naivebayes.traindataset(traininginput, trainingoutput)
	
	# PREDICTION
	# read testing csvs
	testinginput = datahandler.csvtolist("datasets/iris/testing-iris-input.csv")
	#float csv problem
	testinginput = datahandler.tofloat(testinginput)
	# normalisation
	min = datahandler.matrixmin(testinginput)
	max = datahandler.matrixmax(testinginput)
	testinginput = datahandler.normalise(testinginput, max, min)
	predicts = naivebayes.datasetprediction(testinginput, training)
	print(predicts)

if __name__ == '__main__':
	main()