import streamlit as st
import math

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>⚖️ BMI & Diet Plan</h1>
        <p>Calculate your BMI and get a personalized nutrition plan</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📋 Your Details")
        name   = st.text_input("Name (optional)", placeholder="Your name")
        age    = st.number_input("Age", min_value=10, max_value=100, value=25)
        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
        weight = st.number_input("Weight (kg)", min_value=20,  max_value=300, value=70)
        activity = st.selectbox("Activity Level", [
            "Sedentary (desk job, no exercise)",
            "Lightly Active (1-3 days/week)",
            "Moderately Active (3-5 days/week)",
            "Very Active (6-7 days/week)",
            "Extra Active (athlete / physical job)",
        ])
        goal = st.selectbox("Goal", ["🔻 Lose Weight", "⚖️ Maintain Weight", "📈 Gain Muscle"])
        calculate = st.button("⚖️ Calculate My Plan", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if calculate:
            # BMI
            h_m  = height / 100
            bmi  = weight / (h_m ** 2)

            if bmi < 18.5:
                bmi_cat, bmi_color = "Underweight", "#3498db"
            elif bmi < 25:
                bmi_cat, bmi_color = "Normal Weight ✅", "#27ae60"
            elif bmi < 30:
                bmi_cat, bmi_color = "Overweight", "#f39c12"
            else:
                bmi_cat, bmi_color = "Obese", "#e74c3c"

            # BMR (Mifflin-St Jeor)
            if gender == "Male":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161

            # TDEE
            activity_multipliers = {
                "Sedentary (desk job, no exercise)": 1.2,
                "Lightly Active (1-3 days/week)": 1.375,
                "Moderately Active (3-5 days/week)": 1.55,
                "Very Active (6-7 days/week)": 1.725,
                "Extra Active (athlete / physical job)": 1.9,
            }
            tdee = bmr * activity_multipliers[activity]

            # Goal calories
            if "Lose" in goal:
                target_cal = tdee - 500
                protein_g  = round(weight * 2.0)
                fat_g      = round(target_cal * 0.25 / 9)
                carbs_g    = round((target_cal - protein_g * 4 - fat_g * 9) / 4)
                goal_note  = "500 kcal deficit for ~0.5kg/week loss"
            elif "Maintain" in goal:
                target_cal = tdee
                protein_g  = round(weight * 1.6)
                fat_g      = round(target_cal * 0.30 / 9)
                carbs_g    = round((target_cal - protein_g * 4 - fat_g * 9) / 4)
                goal_note  = "Maintenance calories"
            else:
                target_cal = tdee + 300
                protein_g  = round(weight * 2.2)
                fat_g      = round(target_cal * 0.28 / 9)
                carbs_g    = round((target_cal - protein_g * 4 - fat_g * 9) / 4)
                goal_note  = "300 kcal surplus for lean muscle gain"

            target_cal = round(target_cal)
            carbs_g    = max(carbs_g, 50)

            # Display results
            st.markdown(f"""
            <div class="card" style="text-align:center; border-top: 4px solid {bmi_color};">
                <div style="font-size:0.9rem; color:#888;">Your BMI</div>
                <div style="font-size:3rem; font-weight:900; color:{bmi_color};">{bmi:.1f}</div>
                <div style="font-size:1.1rem; font-weight:600; color:{bmi_color};">{bmi_cat}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            c1.metric("🔥 BMR",  f"{round(bmr)} kcal/day")
            c2.metric("⚡ TDEE", f"{round(tdee)} kcal/day")

            st.markdown(f"""
            <div class="card" style="border-top: 4px solid #2d6a4f;">
                <h3>🎯 Your Daily Targets — {goal}</h3>
                <p style="color:#666; font-size:0.85rem;">{goal_note}</p>
                <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:12px;">
                    <div style="flex:1; background:#f0faf4; border-radius:10px; padding:14px; text-align:center;">
                        <div style="font-size:0.8rem; color:#666;">🔥 Calories</div>
                        <div style="font-size:1.6rem; font-weight:700; color:#2d6a4f;">{target_cal}</div>
                        <div style="font-size:0.75rem; color:#888;">kcal/day</div>
                    </div>
                    <div style="flex:1; background:#f0faf4; border-radius:10px; padding:14px; text-align:center;">
                        <div style="font-size:0.8rem; color:#666;">💪 Protein</div>
                        <div style="font-size:1.6rem; font-weight:700; color:#2d6a4f;">{protein_g}g</div>
                        <div style="font-size:0.75rem; color:#888;">per day</div>
                    </div>
                    <div style="flex:1; background:#f0faf4; border-radius:10px; padding:14px; text-align:center;">
                        <div style="font-size:0.8rem; color:#666;">🍞 Carbs</div>
                        <div style="font-size:1.6rem; font-weight:700; color:#2d6a4f;">{carbs_g}g</div>
                        <div style="font-size:0.75rem; color:#888;">per day</div>
                    </div>
                    <div style="flex:1; background:#f0faf4; border-radius:10px; padding:14px; text-align:center;">
                        <div style="font-size:0.8rem; color:#666;">🧈 Fat</div>
                        <div style="font-size:1.6rem; font-weight:700; color:#2d6a4f;">{fat_g}g</div>
                        <div style="font-size:0.75rem; color:#888;">per day</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Ideal weight range
            ideal_low  = round(18.5 * h_m ** 2, 1)
            ideal_high = round(24.9 * h_m ** 2, 1)
            diff = weight - ((ideal_low + ideal_high) / 2)
            diff_str = f"{abs(diff):.1f}kg {'to lose' if diff > 0 else 'to gain'} for ideal weight" if abs(diff) > 1 else "You are at ideal weight!"

            st.markdown(f"""
            <div class="card">
                <b>📏 Ideal Weight Range:</b> {ideal_low} – {ideal_high} kg<br>
                <span style="color:#2d6a4f;">{diff_str}</span>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card" style="text-align:center; padding:60px 20px;">
                <div style="font-size:4rem;">⚖️</div>
                <h3>Fill in your details and click Calculate</h3>
                <p style="color:#888;">Get your BMI, daily calorie needs, and personalized macro targets</p>
            </div>
            """, unsafe_allow_html=True)
