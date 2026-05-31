import streamlit as st
from PIL import Image
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.model_utils import predict_image, get_nutrition

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>🔍 Food Analyzer</h1>
        <p>Upload a food photo to identify it and get complete nutritional information</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📸 Upload Food Image")
        uploaded = st.file_uploader("Choose a food image", type=["jpg", "jpeg", "png", "webp"])
        weight   = st.number_input("🍽️ Portion weight (grams)", min_value=10, max_value=2000, value=100, step=10)

        # Validate file size
        if uploaded and uploaded.size > 10 * 1024 * 1024:  # 10MB limit
            st.error("⚠️ Image file is too large (max 10MB)")
            uploaded = None

        analyze  = st.button("🔍 Analyze Food", use_container_width=True, disabled=uploaded is None)
        st.markdown('</div>', unsafe_allow_html=True)

        if uploaded:
            img = Image.open(uploaded)
            st.image(img, caption="Uploaded Image", use_container_width=True)

    with col2:
        if uploaded and analyze:
            img = Image.open(uploaded)
            with st.spinner("🧠 Analyzing your food..."):
                results, err = predict_image(img, top_k=5)

            if err:
                st.error(f"⚠️ {err}")
            elif results:
                top  = results[0]
                conf = top["prob"] * 100

                st.markdown(f"""
                <div class="result-box">
                    <div style="font-size:1rem; color:#666; margin-bottom:4px;">Predicted Food</div>
                    <div class="food-name">🍽️ {top["display"]}</div>
                    <div class="confidence-badge">✅ {conf:.1f}% Confidence</div>
                </div>
                """, unsafe_allow_html=True)

                st.session_state["last_food"]         = top["class"]
                st.session_state["last_food_display"] = top["display"]
                st.session_state["last_weight"]       = weight

                nutrition = get_nutrition(top["class"], weight)
                if nutrition:
                    st.markdown("---")
                    st.markdown("### 🥦 Nutritional Breakdown")
                    c1, c2, c3 = st.columns(3)
                    c1.metric("🔥 Calories", f"{nutrition['calories']} kcal")
                    c2.metric("💪 Protein",  f"{nutrition['protein']}g")
                    c3.metric("🍞 Carbs",    f"{nutrition['carbs']}g")
                    c4, c5 = st.columns(2)
                    c4.metric("🧈 Fat",   f"{nutrition['fat']}g")
                    c5.metric("🌾 Fiber", f"{nutrition['fiber']}g")

                    st.markdown("**Daily Value (based on 2000 kcal diet)**")
                    st.progress(min(nutrition['calories'] / 2000, 1.0), f"Calories: {nutrition['calories']}/2000 kcal")
                    st.progress(min(nutrition['protein']  / 50,   1.0), f"Protein: {nutrition['protein']}/50g")
                    st.progress(min(nutrition['carbs']    / 275,  1.0), f"Carbs: {nutrition['carbs']}/275g")
                    st.progress(min(nutrition['fat']      / 78,   1.0), f"Fat: {nutrition['fat']}/78g")

                    st.markdown("<br>", unsafe_allow_html=True)
                    if st.button("➕ Add to Meal Tracker", use_container_width=True):
                        if "meal_log" not in st.session_state:
                            st.session_state.meal_log = []
                        st.session_state.meal_log.append({
                            "date":     str(__import__("datetime").date.today()),
                            "meal":     "🍽️ Analyzed",
                            "food":     top["display"],
                            "weight":   weight,
                            "calories": nutrition["calories"],
                            "protein":  nutrition["protein"],
                            "carbs":    nutrition["carbs"],
                            "fat":      nutrition["fat"],
                            "fiber":    nutrition["fiber"],
                        })
                        st.success(f"✅ {top['display']} added to Meal Tracker!")
                else:
                    st.info("Nutrition data not available for this food.")

                st.markdown("**Top 5 Predictions**")
                for i, r in enumerate(results):
                    st.progress(r["prob"], f"#{i+1} {r['display']} — {r['prob']*100:.1f}%")

        elif not uploaded:
            st.markdown("""
            <div class="card" style="text-align:center; padding:60px 20px;">
                <div style="font-size:4rem;">📸</div>
                <h3>Upload a food image to get started</h3>
                <p style="color:#888;">Supports JPG, PNG, WEBP formats</p>
                <p style="color:#888;">Works best with clear, well-lit food photos</p>
                <p style="color:#aaa; font-size:0.85rem;">Best foods: Pizza, Burger, Sushi, Steak, Ramen, Tacos, Donuts, Waffles, Ice Cream, Pancakes...</p>
            </div>
            """, unsafe_allow_html=True)
