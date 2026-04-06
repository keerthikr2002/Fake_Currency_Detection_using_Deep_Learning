import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def train_now():
    # 1. Setup Data Pipeline for Deep Folders (Real/10, Real/50, etc.)
    # We use 20% of your 8GB data for validation to prove accuracy
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

    # Automatically finds images in all nested sub-folders
    train_gen = datagen.flow_from_directory(
        'dataset/',
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary',
        subset='training',
        shuffle=True
    )

    # 2. Modern CNN Architecture (Optimized for Indian Currency)
    model = models.Sequential([
        layers.Input(shape=(128, 128, 3)),
        layers.Conv2D(32, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5), # Crucial for large datasets to prevent memorization
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    print(f"Classes detected: {train_gen.class_indices}")
    print("Training started... this may take time due to the 8GB dataset.")
    
    # 3. Training (10 Epochs is standard for a B.Tech project)
    model.fit(train_gen, epochs=10)

    # 4. Save Logic (Ensures folder exists)
    if not os.path.exists('model'): os.makedirs('model')
    
    # Save Architecture
    with open("model/model.json", "w") as json_file:
        json_file.write(model.to_json())
    
    # Save Weights
    model.save_weights("model/model_weights.h5")
    print("\nSUCCESS: AI Model saved in 'model/' folder. You can now run main.py")

if __name__ == "__main__":
    train_now()