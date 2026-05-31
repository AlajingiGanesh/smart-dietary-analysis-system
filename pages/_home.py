import streamlit as st

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>🥗 Smart Dietary Analysis System</h1>
        <p>AI-powered food recognition & personalized nutrition insights — Final Year Project</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    for col, label, val in zip(
        [col1, col2, col3, col4],
        ["🎯 Accuracy", "🍽️ Food Classes", "🧠 Model", "📊 F1 Score"],
        ["87.62%", "101", "EfficientNetV2-S", "0.876"]
    ):
        with col:
            st.markdown(f'<div class="metric-card"><h3>{label}</h3><h2>{val}</h2></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("""
        <div class="card">
            <h3>🚀 What You Can Do</h3>
            <p>
            <span class="tag">📸 Upload Food Photo</span>
            <span class="tag">🔍 Identify Food Instantly</span><br><br>
            <span class="tag">🥦 Get Nutrition Info</span>
            <span class="tag">⚖️ BMI Analysis</span><br><br>
            <span class="tag">📅 Track Daily Meals</span>
            <span class="tag">🥗 Diet Recommendations</span>
            </p>
            <p style="color:#4a4a4a; font-size:0.95rem; margin-top:12px;">
            Upload any food image and our AI model will instantly identify it from 
            <b>101 different food categories</b> and provide complete nutritional breakdown.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="card">
            <h3>📖 How To Use</h3>
            <ol style="color:#4a4a4a; line-height:2.2rem;">
                <li>Go to <b>🔍 Food Analyzer</b> — upload a food photo</li>
                <li>AI identifies the food with confidence score</li>
                <li>Enter portion weight to get exact nutrition</li>
                <li>Check <b>📊 Nutrition Info</b> for full database</li>
                <li>Use <b>⚖️ BMI Calculator</b> for your diet plan</li>
                <li>Log meals in <b>📅 Meal Tracker</b> daily</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>🎓 About This Project</h3>
        <p style="color:#4a4a4a; font-size:0.95rem; line-height:1.8rem;">
        This <b>Smart Dietary Analysis System</b> is a Final Year Project that uses deep learning to help users 
        make informed dietary decisions. The model was trained on the <b>Food-101 dataset</b> (101,000 images, 101 classes) 
        using <b>EfficientNetV2-S</b> architecture with MixUp augmentation, GeM pooling, two-phase fine-tuning, 
        and Test-Time Augmentation (TTA), achieving <b>87.62% test accuracy</b> — exceeding the 65% project threshold.
        </p>
    </div>
    """, unsafe_allow_html=True)
