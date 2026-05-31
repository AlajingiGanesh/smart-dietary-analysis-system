import json
import streamlit as st
from pathlib import Path

BASE_DIR   = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

NUTRITION_DATA = {
    "apple_pie":              (237, 2.4, 34.0, 11.0, 1.6),
    "baby_back_ribs":         (250, 20.0, 5.0, 17.0, 0.0),
    "baklava":                (428, 6.0, 43.0, 27.0, 2.0),
    "beef_carpaccio":         (121, 20.0, 0.5, 4.5, 0.0),
    "beef_tartare":           (130, 20.5, 1.0, 5.0, 0.0),
    "beet_salad":             (70, 2.0, 10.0, 2.5, 2.5),
    "beignets":               (350, 5.0, 42.0, 18.0, 1.0),
    "bibimbap":               (150, 8.0, 20.0, 4.5, 2.0),
    "bread_pudding":          (230, 5.5, 33.0, 9.0, 0.8),
    "breakfast_burrito":      (200, 9.0, 20.0, 9.5, 1.5),
    "bruschetta":             (160, 4.0, 18.0, 8.0, 1.5),
    "caesar_salad":           (95, 5.0, 5.0, 7.0, 1.5),
    "cannoli":                (310, 7.0, 32.0, 18.0, 0.5),
    "caprese_salad":          (110, 7.0, 3.0, 8.0, 0.5),
    "carrot_cake":            (310, 4.0, 45.0, 14.0, 1.0),
    "ceviche":                (90, 14.0, 5.0, 1.5, 0.5),
    "cheese_plate":           (350, 22.0, 2.0, 28.0, 0.0),
    "cheesecake":             (321, 6.0, 26.0, 22.0, 0.3),
    "chicken_curry":          (150, 12.0, 8.0, 8.5, 1.5),
    "chicken_quesadilla":     (240, 13.0, 19.0, 13.0, 1.0),
    "chicken_wings":          (290, 27.0, 0.0, 19.0, 0.0),
    "chocolate_cake":         (370, 5.0, 50.0, 18.0, 2.0),
    "chocolate_mousse":       (225, 4.5, 23.0, 13.5, 1.5),
    "churros":                (390, 4.5, 45.0, 22.0, 1.0),
    "clam_chowder":           (95, 4.0, 9.0, 5.0, 0.5),
    "club_sandwich":          (210, 14.0, 16.0, 10.0, 1.0),
    "crab_cakes":             (190, 14.0, 10.0, 10.0, 0.5),
    "creme_brulee":           (260, 4.0, 26.0, 16.0, 0.0),
    "croque_madame":          (280, 16.0, 18.0, 16.0, 1.0),
    "cup_cakes":              (305, 3.5, 45.0, 13.0, 0.5),
    "deviled_eggs":           (195, 11.0, 2.0, 16.0, 0.0),
    "donuts":                 (400, 5.0, 50.0, 20.0, 1.0),
    "dumplings":              (200, 8.0, 25.0, 8.0, 1.0),
    "edamame":                (122, 11.0, 10.0, 5.0, 5.0),
    "eggs_benedict":          (240, 12.0, 15.0, 15.0, 0.5),
    "escargots":              (110, 16.0, 2.0, 4.0, 0.0),
    "falafel":                (333, 13.0, 32.0, 18.0, 4.0),
    "filet_mignon":           (210, 28.0, 0.0, 10.0, 0.0),
    "fish_and_chips":         (250, 12.0, 24.0, 12.0, 2.0),
    "foie_gras":              (462, 11.0, 4.0, 44.0, 0.0),
    "french_fries":           (312, 3.5, 41.0, 15.0, 3.8),
    "french_onion_soup":      (55, 2.5, 6.0, 2.5, 0.8),
    "french_toast":           (230, 7.0, 28.0, 10.0, 0.8),
    "fried_calamari":         (175, 15.0, 8.0, 9.0, 0.3),
    "fried_rice":             (170, 5.0, 25.0, 5.5, 1.0),
    "frozen_yogurt":          (127, 3.5, 22.0, 3.0, 0.0),
    "garlic_bread":           (350, 7.0, 40.0, 18.0, 2.0),
    "gnocchi":                (135, 3.0, 27.0, 1.0, 1.5),
    "greek_salad":            (80, 4.0, 5.0, 6.0, 1.5),
    "grilled_cheese_sandwich":(320, 13.0, 28.0, 18.0, 1.0),
    "grilled_salmon":         (208, 25.0, 0.0, 12.0, 0.0),
    "guacamole":              (160, 2.0, 9.0, 14.0, 7.0),
    "gyoza":                  (210, 8.0, 24.0, 9.0, 1.0),
    "hamburger":              (250, 15.0, 20.0, 12.0, 1.0),
    "hot_and_sour_soup":      (45, 3.0, 5.0, 1.5, 0.5),
    "hot_dog":                (290, 10.0, 22.0, 18.0, 0.8),
    "huevos_rancheros":       (160, 9.0, 12.0, 9.0, 2.5),
    "hummus":                 (166, 8.0, 14.0, 10.0, 6.0),
    "ice_cream":              (207, 3.5, 24.0, 11.0, 0.5),
    "lasagna":                (135, 8.0, 12.0, 6.0, 1.0),
    "lobster_bisque":         (120, 5.0, 8.0, 8.0, 0.3),
    "lobster_roll_sandwich":  (200, 12.0, 18.0, 9.0, 1.0),
    "macaroni_and_cheese":    (260, 10.0, 26.0, 13.0, 1.0),
    "macarons":               (400, 6.0, 52.0, 19.0, 1.5),
    "miso_soup":              (30, 2.5, 3.0, 1.0, 0.5),
    "mussels":                (86, 12.0, 4.0, 2.5, 0.0),
    "nachos":                 (340, 9.0, 38.0, 17.0, 3.0),
    "omelette":               (154, 11.0, 1.5, 12.0, 0.0),
    "onion_rings":            (330, 4.0, 40.0, 17.0, 2.0),
    "oysters":                (68, 7.0, 4.0, 2.5, 0.0),
    "pad_thai":               (165, 8.0, 22.0, 5.5, 1.0),
    "paella":                 (140, 7.0, 18.0, 4.5, 1.0),
    "pancakes":               (227, 6.0, 28.0, 10.0, 1.0),
    "panna_cotta":            (240, 3.0, 22.0, 16.0, 0.0),
    "peking_duck":            (270, 18.0, 5.0, 20.0, 0.5),
    "pho":                    (55, 4.0, 6.0, 1.5, 0.5),
    "pizza":                  (266, 11.0, 33.0, 10.0, 2.0),
    "pork_chop":              (231, 25.0, 0.0, 14.0, 0.0),
    "poutine":                (260, 8.0, 28.0, 13.0, 2.0),
    "prime_rib":              (290, 24.0, 0.0, 21.0, 0.0),
    "pulled_pork_sandwich":   (215, 15.0, 18.0, 9.0, 1.0),
    "ramen":                  (110, 7.0, 14.0, 3.0, 1.0),
    "ravioli":                (190, 8.0, 24.0, 7.0, 1.5),
    "red_velvet_cake":        (350, 4.0, 46.0, 17.0, 0.5),
    "risotto":                (140, 4.0, 22.0, 4.0, 0.5),
    "samosa":                 (260, 5.0, 30.0, 14.0, 2.5),
    "sashimi":                (127, 26.0, 0.0, 2.0, 0.0),
    "scallops":               (88, 17.0, 3.0, 0.8, 0.0),
    "seaweed_salad":          (70, 2.0, 9.0, 3.0, 1.0),
    "shrimp_and_grits":       (150, 10.0, 14.0, 6.0, 0.5),
    "spaghetti_bolognese":    (130, 7.0, 16.0, 4.5, 1.5),
    "spaghetti_carbonara":    (190, 9.0, 22.0, 8.0, 1.0),
    "spring_rolls":           (200, 5.0, 24.0, 10.0, 1.5),
    "steak":                  (271, 26.0, 0.0, 18.0, 0.0),
    "strawberry_shortcake":   (260, 3.0, 36.0, 12.0, 1.5),
    "sushi":                  (150, 6.0, 25.0, 3.0, 0.5),
    "tacos":                  (210, 10.0, 20.0, 10.0, 2.0),
    "takoyaki":               (170, 7.0, 20.0, 7.0, 0.5),
    "tiramisu":               (280, 5.0, 30.0, 16.0, 0.5),
    "tuna_tartare":           (115, 23.0, 1.0, 2.0, 0.0),
    "waffles":                (290, 7.0, 33.0, 15.0, 1.0),
}


@st.cache_resource
def load_class_names():
    p = MODELS_DIR / "class_names.json"
    if p.exists():
        with open(p) as f:
            return json.load(f)
    return sorted(NUTRITION_DATA.keys())


@st.cache_resource
def load_model():
    try:
        import torch
        import torch.nn as nn
        import torch.nn.functional as F
        from torchvision.models import efficientnet_v2_s

        model_path = MODELS_DIR / "food_classifier.pt"
        if not model_path.exists():
            return None, "Model file not found. Place food_classifier.pt in the models/ folder."

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        state  = torch.load(str(model_path), map_location=device, weights_only=True)

        class GeM(nn.Module):
            def __init__(self, p=3.0, eps=1e-6):
                super().__init__()
                self.p   = nn.Parameter(torch.ones(1) * p)
                self.eps = eps
            def forward(self, x):
                return F.adaptive_avg_pool2d(
                    x.clamp(min=self.eps).pow(self.p), 1
                ).pow(1.0 / self.p)

        backbone = efficientnet_v2_s(weights=None)
        backbone.avgpool = GeM()
        backbone.classifier = nn.Sequential(
            nn.BatchNorm1d(1280),
            nn.SiLU(),
            nn.Linear(1280, 512),
            nn.Dropout(p=0.3),
            nn.BatchNorm1d(512),
            nn.SiLU(),
            nn.Linear(512, 101),
        )

        backbone.load_state_dict(state, strict=True)
        backbone.to(device)
        backbone.eval()
        return backbone, None

    except ImportError:
        return None, "PyTorch not installed. Run: pip install torch torchvision"
    except Exception as e:
        return None, f"Model load error: {str(e)}"


def predict_image(pil_img, top_k=5):
    try:
        import torch
        import torchvision.transforms as T

        if pil_img is None:
            return None, "No image provided"

        model, err = load_model()
        if model is None:
            return None, err

        class_names = load_class_names()
        device = next(model.parameters()).device

        transform = T.Compose([
            T.Resize((320, 320)),
            T.CenterCrop(300),
            T.ToTensor(),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])

        img_t = transform(pil_img.convert("RGB")).unsqueeze(0).to(device)
        with torch.no_grad():
            logits = model(img_t)
            probs  = torch.softmax(logits, dim=1)[0]
            top_probs, top_idxs = torch.topk(probs, min(top_k, len(class_names)))

        results = []
        for prob, idx in zip(top_probs.cpu().tolist(), top_idxs.cpu().tolist()):
            name = class_names[idx]
            results.append({
                "class":   name,
                "display": name.replace("_", " ").title(),
                "prob":    float(prob)
            })
        return results, None

    except Exception as e:
        return None, f"Prediction error: {str(e)}"


def get_nutrition(class_name, weight_g=100):
    if class_name in NUTRITION_DATA:
        kcal, protein, carbs, fat, fiber = NUTRITION_DATA[class_name]
        scale = weight_g / 100.0
        return {
            "calories": round(kcal * scale),
            "protein":  round(protein * scale, 1),
            "carbs":    round(carbs * scale, 1),
            "fat":      round(fat * scale, 1),
            "fiber":    round(fiber * scale, 1),
        }
    return None


def calculate_daily_stats(meals_list):
    if not meals_list:
        return None
    return {
        "calories":             sum(m.get("calories", 0) for m in meals_list),
        "protein":              sum(m.get("protein", 0)  for m in meals_list),
        "carbs":                sum(m.get("carbs", 0)    for m in meals_list),
        "fat":                  sum(m.get("fat", 0)      for m in meals_list),
        "fiber":                sum(m.get("fiber", 0)    for m in meals_list),
        "meal_count":           len(meals_list),
    }
