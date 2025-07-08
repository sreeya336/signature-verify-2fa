import tensorflow as tf
from tensorflow.keras import layers, Model

# ✅ Correct Registration for your version
@tf.keras.utils.register_keras_serializable()
def l1_distance(vectors):
    x, y = vectors
    return tf.abs(x - y)

def build_base_cnn(input_shape):
    model = tf.keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dense(128, activation='relu')
    ])
    return model

input_shape = (128, 128, 1)
base_cnn = build_base_cnn(input_shape)

input_a = layers.Input(shape=input_shape)
input_b = layers.Input(shape=input_shape)

feat_a = base_cnn(input_a)
feat_b = base_cnn(input_b)

l1_layer = layers.Lambda(l1_distance, output_shape=(128,))
l1_output = l1_layer([feat_a, feat_b])

output = layers.Dense(1, activation='sigmoid')(l1_output)

siamese_model = Model(inputs=[input_a, input_b], outputs=output)

# ✅ Save in Keras format (.keras)
siamese_model.save('siamese_model.keras')

print("✅ Model with registered Lambda saved successfully!")
