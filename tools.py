import pandas as pd 
# need a function to write out the transformed data to a csv
# NOTE this function should be altered to write datafile into a specific directory
def write_csv(input_data, specified_filename):

	# turn input_data into a pandas dataframe
	df = pd.DataFrame(input_data)

	# write it out
	df.to_csv(path_or_buf=specified_filename , sep=',' , index=False, header=None)



