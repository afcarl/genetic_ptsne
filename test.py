from core import Parametric_tSNE
import pandas as pd
from pathlib import Path
import tools

datapath = Path.cwd() / 'RBMTrainingDataset' / 'training_set.csv'

data = pd.read_csv(str(datapath) , sep=',' , header=None)
high_dims = data.shape[1]
num_outputs = 2
perplexity = 30

train_data = data.values

#test_data = pd.read_csv(str(Path.cwd() / 'RBMTrainingDataset' / '2018_data.csv') , sep=',' , header=None)
#test_data = test_data.values

ptSNE = Parametric_tSNE(high_dims, num_outputs, perplexity, all_layers=[100,50])
ptSNE.fit(train_data, verbose=1)
#x = ptSNE.transform(test_data)
#tools.write_csv(x , 'transformed_data.csv')

#ptSNE.save_model(str(Path.cwd() / 'Models' / 'testmodel'))

print('done')
