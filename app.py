import streamlit as st

st.set_page_config(
    page_title="Smart Dietary Analysis System",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');
:root {
    --green-dark: #1a3a2a;
    --green-mid: #2d6a4f;
    --green-light: #52b788;
    --green-pale: #b7e4c7;
    --cream: #f8f4e9;
}
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream);
}
[data-testid="stSidebar"] {
    background: var(--green-dark) !important;
    border-right: 3px solid var(--green-light);
}
[data-testid="stSidebar"] * { color: #e8f5e9 !important; }
h1, h2, h3 { font-family: 'Playfair Display', serif !important; }
.card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 24px rgba(26,58,42,0.10);
    border: 1px solid #e8f5e9;
    margin-bottom: 16px;
}
.metric-card {
    background: linear-gradient(135deg, var(--green-mid), var(--green-dark));
    color: white !important;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}
.metric-card h3 { color: var(--green-pale) !important; font-size: 0.85rem !important; margin: 0 !important; }
.metric-card h2 { color: white !important; font-size: 1.8rem !important; margin: 4px 0 0 0 !important; }
.result-box {
    background: linear-gradient(135deg, #f0faf4, #e8f5e9);
    border: 2px solid var(--green-light);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
}
.food-name {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--green-dark);
}
.confidence-badge {
    display: inline-block;
    background: var(--green-mid);
    color: white;
    border-radius: 20px;
    padding: 4px 16px;
    font-size: 0.85rem;
    margin-top: 6px;
}
.stButton > button {
    background: linear-gradient(135deg, var(--green-mid), var(--green-dark)) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 28px !important;
    font-weight: 600 !important;
    width: 100%;
}
.header-banner {
    background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-mid) 60%, var(--green-light) 100%);
    border-radius: 20px;
    padding: 32px 40px;
    margin-bottom: 28px;
}
.header-banner h1 { color: white !important; font-size: 2.2rem !important; margin: 0 !important; }
.header-banner p { color: var(--green-pale) !important; margin: 6px 0 0 0 !important; }
.tag {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green-dark);
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 2px;
}
.log-item {
    background: white;
    border-radius: 10px;
    padding: 12px 16px;
    margin: 6px 0;
    border: 1px solid #e8f5e9;
    display: flex;
    justify-content: space-between;
}
div[data-testid="stMetric"] {
    background: white;
    border-radius: 12px;
    padding: 14px !important;
    border: 1px solid #e8f5e9;
    box-shadow: 0 4px 24px rgba(26,58,42,0.08);
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🥗 Smart Dietary\n### Analysis System")
    st.markdown("---")
    page = st.radio("Navigate", [
        "🏠 Home",
        "🔍 Food Analyzer",
        "📊 Nutrition Info",
        "⚖️ BMI & Diet Plan",
        "📅 Meal Tracker",
        "📈 Analytics",
    ])
    st.markdown("---")
    st.markdown("**Model Info**")
    st.markdown("- EfficientNetV2-S")
    st.markdown("- 101 Food Classes")
    st.markdown("- **87.62% Accuracy**")
    st.markdown("- F1 Score: 0.876")

page_name = page.split(" ", 1)[1].strip()

if page_name == "Home":
    from pages._home import show; show()
elif page_name == "Food Analyzer":
    from pages._food_analyzer import show; show()
elif page_name == "Nutrition Info":
    from pages._nutrition import show; show()
elif page_name == "BMI & Diet Plan":
    from pages._bmi import show; show()
elif page_name == "Meal Tracker":
    from pages._meal_tracker import show; show()
elif page_name == "Analytics":
    from pages._analytics import show; show()
