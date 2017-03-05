class Hyparms():
    def __init__(self):
        pass

HYPARMS = Hyparms()

HYPARMS.batch_size = 128
HYPARMS.learning_rate = 0.1
HYPARMS.max_steps = 5000
HYPARMS.log_dir = 'logs'
HYPARMS.input_data_dir = 'data'
HYPARMS.recog_data_dir = 'input'
HYPARMS.ckpt_dir = 'LetterRecognizer/trained'
HYPARMS.ckpt_name = 'trained_weight'
HYPARMS.dropout_rate = 1