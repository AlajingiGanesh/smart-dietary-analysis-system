import json
import csv
import io
from pathlib import Path

DATA_DIR      = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
MEAL_LOG_FILE = DATA_DIR / "meal_logs.json"


def save_meal_log(meal_log):
    try:
        with open(MEAL_LOG_FILE, "w") as f:
            json.dump(meal_log, f, indent=2)
        return True
    except Exception:
        return False


def load_meal_log():
    try:
        if MEAL_LOG_FILE.exists():
            with open(MEAL_LOG_FILE) as f:
                return json.load(f)
    except Exception:
        pass
    return []


def clear_meal_log():
    try:
        if MEAL_LOG_FILE.exists():
            MEAL_LOG_FILE.unlink()
        return True
    except Exception:
        return False


def export_to_csv(meal_log):
    try:
        if not meal_log:
            return None
        buf = io.StringIO()
        fields = ["Date", "Meal Type", "Food", "Weight (g)",
                  "Calories", "Protein (g)", "Carbs (g)", "Fat (g)", "Fiber (g)"]
        writer = csv.DictWriter(buf, fieldnames=fields)
        writer.writeheader()
        for m in meal_log:
            writer.writerow({
                "Date":        m.get("date", ""),
                "Meal Type":   m.get("meal", ""),
                "Food":        m.get("food", ""),
                "Weight (g)":  m.get("weight", ""),
                "Calories":    m.get("calories", ""),
                "Protein (g)": m.get("protein", ""),
                "Carbs (g)":   m.get("carbs", ""),
                "Fat (g)":     m.get("fat", ""),
                "Fiber (g)":   m.get("fiber", ""),
            })
        return buf.getvalue()
    except Exception:
        return None
