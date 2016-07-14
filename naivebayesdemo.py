#module imports

#my module imports
import datahandler
import naivebayes

def main():
	#read csvs
	dataset = datahandler.csvtolist("datasets/iris/iris-input.csv")
	output = datahandler.csvtolist("datasets/iris/iris-output.csv")
	#normalisation
	min = datahandler.matrixmin(dataset)
	max = datahandler.matrixmax(dataset)
	dataset = datahandler.normalise(dataset, max, min)
	#naive bayes classification
	#train with the dataset
	training = naivebayes.traindataset(dataset, output)
	#test with the same dataset (only for demo purpose)
	predicts = naivebayes.datasetprediction(dataset, training)
	print(predicts)

if __name__ == '__main__':
	main()