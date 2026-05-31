import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.model_utils import NUTRITION_DATA

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>📊 Nutrition Information</h1>
        <p>Browse and compare nutritional data for all 101 food categories</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("🔍 Search food", placeholder="e.g. pizza, sushi, burger...")
    with col2:
        portion = st.number_input("Portion weight (g)", min_value=10, max_value=1000, value=100, step=10)

    # Filter foods
    all_foods = sorted(NUTRITION_DATA.keys())
    if search:
        all_foods = [f for f in all_foods if search.lower() in f.replace("_", " ").lower()]

    st.markdown(f"**Showing {len(all_foods)} foods**")

    # Display cards in 3 columns
    cols = st.columns(3)
    for i, food_key in enumerate(all_foods):
        kcal, protein, carbs, fat, fiber = NUTRITION_DATA[food_key]
        scale = portion / 100.0
        display_name = food_key.replace("_", " ").title()

        with cols[i % 3]:
            st.markdown(f"""
            <div class="card" style="border-left: 4px solid #52b788; padding: 16px; margin-bottom: 12px;">
                <div style="font-weight:700; font-size:1rem; color:#1a3a2a;">{display_name}</div>
                <div style="color:#888; font-size:0.8rem; margin-bottom:8px;">per {portion}g</div>
                <div style="font-size:1.4rem; font-weight:700; color:#2d6a4f;">{round(kcal*scale)} kcal</div>
                <div style="margin-top:6px;">
                    <span class="tag">P: {round(protein*scale,1)}g</span>
                    <span class="tag">C: {round(carbs*scale,1)}g</span>
                    <span class="tag">F: {round(fat*scale,1)}g</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Compare section
    st.markdown("---")
    st.markdown("### ⚖️ Compare Two Foods")
    food_options = [f.replace("_", " ").title() for f in sorted(NUTRITION_DATA.keys())]
    food_keys    = sorted(NUTRITION_DATA.keys())

    c1, c2 = st.columns(2)
    with c1:
        sel1 = st.selectbox("Food 1", food_options, index=food_options.index("Pizza"))
    with c2:
        sel2 = st.selectbox("Food 2", food_options, index=food_options.index("Hamburger"))

    key1 = food_keys[food_options.index(sel1)]
    key2 = food_keys[food_options.index(sel2)]
    n1   = NUTRITION_DATA[key1]
    n2   = NUTRITION_DATA[key2]
    labels = ["Calories (kcal)", "Protein (g)", "Carbs (g)", "Fat (g)", "Fiber (g)"]

    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown(f'<div class="card" style="border-top:4px solid #2d6a4f;">', unsafe_allow_html=True)
        st.markdown(f"**{sel1}** (per 100g)")
        for label, val in zip(labels, n1):
            st.markdown(f"- {label}: **{val}**")
        st.markdown("</div>", unsafe_allow_html=True)
    with cc2:
        st.markdown(f'<div class="card" style="border-top:4px solid #52b788;">', unsafe_allow_html=True)
        st.markdown(f"**{sel2}** (per 100g)")
        for label, val in zip(labels, n2):
            st.markdown(f"- {label}: **{val}**")
        st.markdown("</div>", unsafe_allow_html=True)
