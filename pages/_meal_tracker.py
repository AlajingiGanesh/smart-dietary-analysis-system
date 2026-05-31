import streamlit as st
from datetime import date
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.model_utils import NUTRITION_DATA, get_nutrition
from utils.persistence import save_meal_log, load_meal_log, export_to_csv, clear_meal_log

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>📅 Daily Meal Tracker</h1>
        <p>Log your meals and monitor your daily nutritional intake</p>
    </div>
    """, unsafe_allow_html=True)

    # Load meal log from persistent storage
    if "meal_log" not in st.session_state:
        st.session_state.meal_log = load_meal_log()

    food_keys    = sorted(NUTRITION_DATA.keys())
    food_options = [f.replace("_", " ").title() for f in food_keys]

    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ➕ Add Meal")

        today     = st.date_input("Date", value=date.today())
        meal_time = st.selectbox("Meal", ["🌅 Breakfast", "☀️ Lunch", "🌙 Dinner", "🍎 Snack"])

        # Default to last predicted food if available
        default_idx = 0
        if "last_food_display" in st.session_state:
            try:
                default_idx = food_options.index(st.session_state.last_food_display)
            except ValueError:
                default_idx = 0

        selected_display = st.selectbox("Food Item", food_options, index=default_idx)
        selected_key     = food_keys[food_options.index(selected_display)]
        weight           = st.number_input("Portion (grams)", min_value=10, max_value=2000, value=100, step=10)

        # Show preview nutrition
        kcal, protein, carbs, fat, fiber = NUTRITION_DATA[selected_key]
        scale = weight / 100.0
        st.markdown(f"""
        <div style="background:#f0faf4; border-radius:10px; padding:10px; margin:8px 0; font-size:0.85rem;">
            <b>Preview:</b> {round(kcal*scale)} kcal | P:{round(protein*scale,1)}g | C:{round(carbs*scale,1)}g | F:{round(fat*scale,1)}g
        </div>
        """, unsafe_allow_html=True)

        if st.button("➕ Add to Log", use_container_width=True):
            nutrition = get_nutrition(selected_key, weight)
            if nutrition:
                st.session_state.meal_log.append({
                    "date":     str(today),
                    "meal":     meal_time,
                    "food":     selected_display,
                    "weight":   weight,
                    "calories": nutrition["calories"],
                    "protein":  nutrition["protein"],
                    "carbs":    nutrition["carbs"],
                    "fat":      nutrition["fat"],
                    "fiber":    nutrition["fiber"],
                })
                save_meal_log(st.session_state.meal_log)
                st.success(f"✅ Added {selected_display} ({weight}g)")

        if st.button("🗑️ Clear All Logs", use_container_width=True):
            st.session_state.meal_log = []
            clear_meal_log()
            st.info("Meal log cleared.")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("### 📋 Today's Meal Log")
        today_str   = str(date.today())
        today_meals = [m for m in st.session_state.meal_log if m.get("date") == today_str]

        if not today_meals:
            st.markdown("""
            <div class="card" style="text-align:center; padding:40px;">
                <div style="font-size:3rem;">🍽️</div>
                <p style="color:#888;">No meals logged today.<br>Add your first meal!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            total_cal     = sum(m["calories"] for m in today_meals)
            total_protein = sum(m["protein"]  for m in today_meals)
            total_carbs   = sum(m["carbs"]    for m in today_meals)
            total_fat     = sum(m["fat"]      for m in today_meals)

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("🔥 Calories", f"{total_cal} kcal")
            c2.metric("💪 Protein",  f"{total_protein}g")
            c3.metric("🍞 Carbs",    f"{total_carbs}g")
            c4.metric("🧈 Fat",      f"{total_fat}g")

            st.markdown("**Daily Calorie Goal Progress (2000 kcal)**")
            pct   = min(total_cal / 2000, 1.0)
            note  = "🟢 On track" if pct < 0.85 else ("🟡 Almost at limit" if pct < 1.0 else "🔴 Exceeded!")
            st.progress(pct, f"{total_cal}/2000 kcal — {note}")

            st.markdown("---")
            for meal in today_meals:
                st.markdown(f"""
                <div class="log-item">
                    <div>
                        <b>{meal['meal']} — {meal['food']}</b><br>
                        <small style="color:#888;">{meal['weight']}g</small>
                    </div>
                    <div style="text-align:right;">
                        <b style="color:#2d6a4f;">{meal['calories']} kcal</b><br>
                        <small style="color:#888;">P:{meal['protein']}g C:{meal['carbs']}g F:{meal['fat']}g</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Macro split
            total_macro_cal = (total_protein * 4) + (total_carbs * 4) + (total_fat * 9)
            if total_macro_cal > 0:
                p_pct = round(total_protein * 4 / total_macro_cal * 100)
                c_pct = round(total_carbs   * 4 / total_macro_cal * 100)
                f_pct = round(total_fat     * 9 / total_macro_cal * 100)
                st.markdown("**Macro Split**")
                st.markdown(f"""
                <div class="card">
                    <span class="tag" style="background:#d4f1e4;">💪 Protein {p_pct}%</span>
                    <span class="tag" style="background:#fde9b0;">🍞 Carbs {c_pct}%</span>
                    <span class="tag" style="background:#ffd6d6;">🧈 Fat {f_pct}%</span>
                    <br><br>
                    <small style="color:#888;">Ideal: Protein 25-30% | Carbs 45-50% | Fat 20-30%</small>
                </div>
                """, unsafe_allow_html=True)

            # Export section
            st.markdown("---")
            st.markdown("### 📥 Export Data")
            csv_data = export_to_csv(st.session_state.meal_log)
            if csv_data:
                st.download_button(
                    label="📥 Download Meal Log as CSV",
                    data=csv_data,
                    file_name=f"meal_log_{date.today()}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
