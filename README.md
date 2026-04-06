# 💸 Indian Currency Authenticator: Fake Note Detection using CNN

A Deep Learning-based desktop application designed to identify counterfeit Indian banknotes using Convolutional Neural Networks (CNN). This project utilizes the **Mahatma Gandhi New Series** dataset and achieves high accuracy in distinguishing between real and fake currency.

---

## 🚀 Project Overview

Counterfeit currency is a significant threat to the economy. This project provides a software-based solution to verify the authenticity of Indian banknotes (₹10, ₹50, ₹100, ₹200, ₹500, ₹2000). By leveraging **Computer Vision** and **Deep Learning**, the system analyzes visual security features that are often missed by the human eye.

### Key Features

- **Deep Learning Engine:** Built with TensorFlow/Keras using a custom CNN architecture.
- **Hierarchical Data Processing:** Automatically handles deep-level folders for different denominations.
- **Real-time Prediction:** User-friendly GUI for instant image verification.
- **High Precision:** Achieved **97.6% training accuracy**.

---

## 🧠 Model Architecture

The model uses a sequential CNN approach:

1. **Input Layer:** 128 × 128 × 3 (RGB Images)
2. **Convolutional Layers:** 3 layers with ReLU activation for feature extraction.
3. **Pooling Layers:** Max-pooling to reduce spatial dimensions.
4. **Dropout Layer:** 0.5 dropout to prevent overfitting on the large dataset.
5. **Output Layer:** Sigmoid activation for Binary Classification (Real vs. Fake).

---

## 📸 Project Results & Screenshots

### 1. Model Training Performance

The model was trained on **5,954 images**. As shown in the training logs, the system reached a final accuracy of **97.68%** with a minimal loss of **0.0610**.
```text
Epoch 10/10
187/187 ━━━━━━━━━━━━━━━━━━━━ 45s 241ms/step 
loss: 0.0610 - accuracy: 0.9768 - val_loss: 0.0812 - val_accuracy: 0.9650

SUCCESS: AI Model saved in 'model/' folder.
```

### 2. Live Testing (GUI)

The application successfully identifies denominations from the Mahatma Gandhi New Series. Below is a test result for a **₹500 Note** correctly identified as **Fake**.

![GUI Result](project_screenshots/gui_result.PNG)

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Deep Learning:** TensorFlow 2.16+, Keras 3
- **Computer Vision:** OpenCV (cv2)
- **GUI:** Tkinter
- **Dataset:** Kaggle Indian Currency (Real vs Fake) Dataset

---

## 📂 Project Structure

```text
Fake_Currency_Detection/
├── dataset/               # 8GB Dataset (Real/Fake folders)
├── project_screenshots/   # Screenshots for documentation
├── model/                 
│   ├── model.json         # Saved AI Architecture
│   └── model.weights.h5   # Trained AI Weights
├── fake_currency_detection_using_CNN.pdf    
├── train_model.py         # Script to train the CNN
├── main.py                # GUI Application script
├── requirements.txt       # Necessary libraries
└── README.md              # Project documentation
```

## ⚙️ Setup & Execution

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

```bash
python train_model.py
```

### 3. Run the Application

```bash
python main.py
```

---

## 🎓 Conclusion

This project demonstrates the power of Convolutional Neural Networks in financial security. It successfully automates the detection of counterfeit notes with high confidence, making it a viable prototype for banking and retail applications. By utilizing deep learning, we can identify sophisticated forgeries that traditional methods might overlook.
