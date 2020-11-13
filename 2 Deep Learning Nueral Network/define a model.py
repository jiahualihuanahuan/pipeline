# There are a few ways to define the Sequential model
# import required libraries and modules
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
#---------------------------------------
# 1 use Sequential([...])
# Define Sequential model with 3 layers
model = keras.Sequential(
    [
        layers.Dense(2, activation="relu", name="layer1"),
        layers.Dense(3, activation="relu", name="layer2"),
        layers.Dense(4, name="layer3"),
    ]
)
# Call model on a test input
x = tf.ones((3, 3))
y = model(x)

model.summary()
#---------------------------------------
# 2 use add(...)
model = keras.Sequential()
model.add(keras.layers.Dense(32, activation='relu', name='layer 1', input_shape= (28,28)))
model.add(keras.layers.Dense(16, activation='relu', name='layer 2'))
model.add(keras.layers.Dense(8, activation='relu', name='layer 3'))
model.summary()
# access layers
model.layers
len(model.layers)

# Use pop() method to remove layers
model.pop()
len(model.layers)
model.summary()

#---------------------------------------
# 3 Nested layers

# Create 3 layers
layer1 = layers.Dense(2, activation="relu", name="layer1")
layer2 = layers.Dense(3, activation="relu", name="layer2")
layer3 = layers.Dense(4, name="layer3")

# Call layers on a test input
x = tf.ones((3, 3))
y = layer3(layer2(layer1(x)))

#---------------------------------------
# Layers needs input(input size) to be able to create their weights
layer = layers.Dense(3)
layer.weights  # Empty
# Call layer on a test input
x = tf.ones((1, 4))
y = layer(x)
layer.weights  # Now it has weights, of shape (4, 3) and (3,)
#---------------------------------------
# Specify input shape by Input(shape=(...))
model = keras.Sequential()
model.add(keras.Input(shape=(4,)))
model.add(layers.Dense(2, activation="relu"))

model.summary()

#---------------------------------------
# Debugging model build
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------

#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------
#---------------------------------------