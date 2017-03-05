class Hyparms():
    def __init__(self):
        pass

HYPARMS = Hyparms()

HYPARMS.batch_size = 10
HYPARMS.learning_rate = 0.01
HYPARMS.max_steps = 5000
HYPARMS.log_dir = 'logs'
HYPARMS.input_data_dir = 'data/train'
HYPARMS.recog_data_dir = 'data/test'
HYPARMS.ckpt_dir = 'logs'
HYPARMS.ckpt_name = 'trained_weight'
HYPARMS.dropout_rate = 1