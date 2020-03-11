from tensorflow import keras
from focal_loss import BinaryFocalLoss
from custom_functions import custom_loss
import os

# Constant
ITERATION = 5
BATCH_SIZE = 4
EPOCHS = 50
METRICS = [
      keras.metrics.TruePositives(name='tp'),
      keras.metrics.FalsePositives(name='fp'),
      keras.metrics.TrueNegatives(name='tn'),
      keras.metrics.FalseNegatives(name='fn'), 
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall'),
      keras.metrics.AUC(name='auc'),
]
LR = 1e-3
LOSS = {
      'custom-bce': custom_loss.binary_crossentropy,
      'custom-mse': custom_loss.mean_square_error,
      'custom-mfe': custom_loss.mean_false_error,
      'custom-fl': custom_loss.focal,
      'custom-hybrid-mfe-fl': custom_loss.hybrid_mfe_fl
}
OPTIMIZER = keras.optimizers.Adam(lr=LR)

# Path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
train_set_path = os.path.join(ROOT_DIR, 'train')
test_set_path = os.path.join(ROOT_DIR, 'test')
result_path = os.path.join(ROOT_DIR, 'results')
viz_path = os.path.join(ROOT_DIR, 'visualizations')