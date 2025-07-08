import tensorflow as tf
from tensorflow.keras import layers, Model

# Build base CNN
def build_base_cnn(input_shape):
    model = tf.keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(32, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation='relu')
    ])
    return model

input_shape = (128, 128, 1)

# Siamese architecture
base_cnn = build_base_cnn(input_shape)

input_a = layers.Input(shape=input_shape)
input_b = layers.Input(shape=input_shape)

feat_a = base_cnn(input_a)
feat_b = base_cnn(input_b)

l1_distance = layers.Lambda(lambda tensors: tf.abs(tensors[0] - tensors[1]))([feat_a, feat_b])
output = layers.Dense(1, activation='sigmoid')(l1_distance)

siamese_model = Model(inputs=[input_a, input_b], outputs=output)

# Save model
siamese_model.save('siamese_model.keras')

print("✅ Siamese model saved locally in .keras format!")
