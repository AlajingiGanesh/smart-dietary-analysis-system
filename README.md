# Smart Dietary Analysis System
**Final Year Project** — AI-powered food recognition & nutrition analysis

## Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Place your 4 model files in the `models/` folder:
   - `food_classifier.pt`
   - `class_names.json`
   - `nutrition_lookup.json`
   - `eval_results.json`

3. Run the app:
   ```bash
   python -m streamlit run app.py
   ```

App opens at: **http://localhost:8501**

## Model
- Architecture: EfficientNetV2-S + GeM Pooling
- Dataset: Food-101 (101,000 images, 101 classes)
- Test Accuracy: **87.62%**
- F1 Score: **0.876**
