from src.model import Model
from config.config import HYPARMS
from DataConverter import inputdata


model = Model()

data_sets = inputdata.read_data_sets(HYPARMS.input_data_dir)

model.load_data(data_sets.train, data_sets.test)