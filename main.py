import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tkinter as tk
from tkinter import filedialog, messagebox, END
import cv2
import numpy as np
import os
from keras.models import model_from_json

class CurrencyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Currency Detection System (CNN)")
        self.root.geometry("600x500")
        self.model = None

        # UI Styling
        self.label = tk.Label(root, text="Indian Currency Authenticator", font=("Arial", 16, "bold"))
        self.label.pack(pady=20)

        self.display = tk.Text(root, height=10, width=60, font=("Consolas", 10))
        self.display.pack(pady=10)

        self.btn_load = tk.Button(root, text="1. Load AI Model", command=self.load_model, bg="#add8e6", width=25)
        self.btn_load.pack(pady=5)

        self.btn_check = tk.Button(root, text="2. Upload & Verify Note", command=self.predict, bg="#90ee90", width=25)
        self.btn_check.pack(pady=5)

    def load_model(self):
        try:
            if not os.path.exists('model/model.json'):
                messagebox.showerror("Error", "Model files not found! Run train_model.py first.")
                return

            with open('model/model.json', 'r') as f:
                self.model = model_from_json(f.read())
            self.model.load_weights("model/model.weights.h5")
            self.display.insert(END, "[SYSTEM] CNN Model Loaded Successfully.\n")
        except Exception as e:
            self.display.insert(END, f"[ERROR] Could not load model: {str(e)}\n")

    def predict(self):
        if not self.model:
            messagebox.showwarning("Warning", "Please load the model first!")
            return
        
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            try:
                img = cv2.imread(path)
                if img is None: raise ValueError("Invalid image file")

                # Preprocessing: Must match the 128x128 training size
                process_img = cv2.resize(img, (128, 128))
                img_array = np.array(process_img).reshape(1, 128, 128, 3) / 255.0
                
                prediction = self.model.predict(img_array)
                # 0.5 is the threshold for binary classification
                result = "GENUINE" if prediction[0][0] > 0.5 else "FAKE"
                confidence = prediction[0][0] if result == "GENUINE" else 1 - prediction[0][0]

                # Update Log
                self.display.insert(END, f"File: {os.path.basename(path)}\nResult: {result} ({confidence*100:.2f}%)\n{'-'*30}\n")
                
                # Visual Pop-up
                preview = cv2.resize(img, (500, 350))
                color = (0, 255, 0) if result == "GENUINE" else (0, 0, 255)
                cv2.putText(preview, f"Status: {result}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                cv2.imshow("Analysis Result", preview)
            
            except Exception as e:
                self.display.insert(END, f"[ERROR] Prediction failed: {str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyApp(root)
    root.mainloop()