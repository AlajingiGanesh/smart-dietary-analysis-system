# 🍽️ Smart Dietary Analysis System

### AI-Powered Food Recognition & Nutrition Analysis

An intelligent dietary analysis system that identifies food items from images and provides estimated nutritional information including calories, protein, carbohydrates, and fats using Deep Learning and Computer Vision techniques.

🔗 **Live Demo:**
https://smart-dietary-analysis-system-dg2mhg6pcybwqgrmpbmtaw.streamlit.app/

---

## 📖 Overview

The Smart Dietary Analysis System is a Deep Learning-based web application designed to help users make informed dietary decisions. Users can upload a food image, and the system automatically identifies the food item and provides detailed nutritional insights.

This project combines Computer Vision, Deep Learning, and Nutrition Analysis to create a practical healthcare-focused application that promotes healthy eating habits and nutritional awareness.

---

## 🚀 Key Features

### 📸 Food Recognition

* Upload food images directly through the web interface.
* Automatic food classification using a trained Deep Learning model.
* Supports 101 different food categories.

### 🧠 Deep Learning Powered

* Uses EfficientNetV2-S architecture for high-accuracy image classification.
* Optimized using GeM Pooling for improved feature extraction.
* Achieved strong performance on large-scale food datasets.

### 🍎 Nutritional Analysis

* Estimates:

  * Calories
  * Protein
  * Carbohydrates
  * Fat
* Provides nutritional information instantly after prediction.

### 📊 Confidence Score

* Displays prediction confidence.
* Helps users understand model certainty.

### 🌐 Interactive Web Interface

* Clean and responsive Streamlit-based UI.
* User-friendly workflow requiring no technical knowledge.

### ⚡ Real-Time Predictions

* Fast image processing and instant results.
* Accessible from desktop and mobile browsers.

---

## 🏗️ System Architecture

```text
User Uploads Food Image
            │
            ▼
Image Preprocessing
            │
            ▼
EfficientNetV2-S Model
            │
            ▼
Food Classification
            │
            ▼
Nutrition Lookup Engine
            │
            ▼
Calories & Nutritional Report
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Deep Learning

* PyTorch
* TorchVision

### Computer Vision

* OpenCV
* Pillow

### Data Processing

* NumPy
* Pandas

### Model Architecture

* EfficientNetV2-S
* GeM Pooling

---

## 🤖 Model Information

### Architecture

* EfficientNetV2-S + GeM Pooling

### Dataset

* Food-101 Dataset
* 101 Food Categories
* 101,000 Images

### Performance Metrics

| Metric        | Score          |
| ------------- | -------------- |
| Test Accuracy | 87.62%         |
| F1 Score      | 0.876          |
| Classes       | 101            |
| Dataset Size  | 101,000 Images |

---

## 📂 Project Structure

```text
Smart-Dietary-Analysis-System/
│
├── app.py
├── requirements.txt
├── models/
│   ├── food_classifier.pt
│   ├── class_names.json
│   ├── nutrition_lookup.json
│   └── eval_results.json
│
├── assets/
├── notebooks/
├── README.md
└── screenshots/
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/AlajingiGanesh/Smart-Dietary-Analysis-System.git
cd Smart-Dietary-Analysis-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Required Model Files

Place the following files inside the `models/` directory:

```text
food_classifier.pt
class_names.json
nutrition_lookup.json
eval_results.json
```

Directory structure:

```text
models/
├── food_classifier.pt
├── class_names.json
├── nutrition_lookup.json
└── eval_results.json
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 🌐 Live Deployment

The application is deployed on Streamlit Cloud.

### Live Demo

🔗 https://smart-dietary-analysis-system-dg2mhg6pcybwqgrmpbmtaw.streamlit.app/

No installation required.

Simply open the link, upload a food image, and receive instant nutritional analysis.

---

## 🎯 Use Cases

* Personal Diet Monitoring
* Calorie Tracking
* Nutrition Awareness
* Fitness & Health Management
* Educational Research
* AI in Healthcare Demonstration
* Smart Dietary Recommendations

---

## 🔮 Future Enhancements

### Multi-Food Detection

* Detect multiple food items in a single image.

### Portion Size Estimation

* Estimate serving quantity and improve calorie calculations.

### Personalized Diet Recommendations

* Generate customized meal suggestions.

### Mobile Application

* Android and iOS support.

### Barcode Integration

* Scan packaged foods for nutrition information.

### AI Health Assistant

* Conversational dietary guidance using Generative AI.

### Cloud-Based Analytics

* Track user dietary habits and trends over time.

---

## 🏆 Achievements

* Final Year B.Tech Project
* Built using State-of-the-Art Deep Learning Architecture
* Achieved 87.62% Test Accuracy
* Successfully Deployed on Streamlit Cloud
* Demonstrates practical application of AI in Healthcare

---

## 👨‍💻 Author

### Alajingi Ganesh

B.Tech Computer Science & Engineering
Indian Institute of Information Technology Tiruchirappalli

📧 Email: [ganeshalajingi123@gmail.com](mailto:ganeshalajingi123@gmail.com)

💼 LinkedIn: https://linkedin.com/in/alajingiganesh

💻 GitHub: https://github.com/AlajingiGanesh

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support helps improve and maintain the project.
