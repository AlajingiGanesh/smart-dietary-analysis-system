import streamlit as st
import pandas as pd
from datetime import date, timedelta
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from utils.persistence import load_meal_log
from utils.model_utils import calculate_daily_stats

def show():
    st.markdown("""
    <div class="header-banner">
        <h1>📊 Analytics & Statistics</h1>
        <p>View trends and insights from your meal logging data</p>
    </div>
    """, unsafe_allow_html=True)

    meal_log = load_meal_log()

    if not meal_log:
        st.markdown("""
        <div class="card" style="text-align:center; padding:60px 20px;">
            <div style="font-size:4rem;">📊</div>
            <h3>No data yet</h3>
            <p style="color:#888;">Start logging meals to see analytics</p>
        </div>
        """, unsafe_allow_html=True)
        return

    # Convert to DataFrame for easier analysis
    df = pd.DataFrame(meal_log)
    df['date'] = pd.to_datetime(df['date'])

    # Date range selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=date.today() - timedelta(days=7))
    with col2:
        end_date = st.date_input("End Date", value=date.today())

    # Filter data
    mask = (df['date'].dt.date >= start_date) & (df['date'].dt.date <= end_date)
    filtered_df = df[mask]

    if filtered_df.empty:
        st.warning("No data in selected date range")
        return

    # Overview metrics
    st.markdown("### 📈 Overview")
    col1, col2, col3, col4 = st.columns(4)

    total_meals = len(filtered_df)
    total_calories = filtered_df['calories'].sum()
    avg_calories = round(total_calories / total_meals) if total_meals > 0 else 0
    unique_days = filtered_df['date'].dt.date.nunique()

    col1.metric("🍽️ Total Meals", total_meals)
    col2.metric("🔥 Total Calories", f"{total_calories:,}")
    col3.metric("⌛ Avg/Meal", f"{avg_calories} kcal")
    col4.metric("📅 Days Tracked", unique_days)

    st.markdown("---")

    # Daily trends
    st.markdown("### 📉 Daily Trends")
    daily_stats = filtered_df.groupby(filtered_df['date'].dt.date).agg({
        'calories': 'sum',
        'protein': 'sum',
        'carbs': 'sum',
        'fat': 'sum',
    }).reset_index()
    daily_stats.columns = ['Date', 'Calories', 'Protein', 'Carbs', 'Fat']

    col1, col2 = st.columns(2)

    with col1:
        st.line_chart(daily_stats.set_index('Date')[['Calories']], use_container_width=True)

    with col2:
        st.bar_chart(daily_stats.set_index('Date')[['Protein', 'Carbs', 'Fat']], use_container_width=True)

    st.markdown("---")

    # Macro analysis
    st.markdown("### 🥗 Macro Analysis")
    total_protein = filtered_df['protein'].sum()
    total_carbs = filtered_df['carbs'].sum()
    total_fat = filtered_df['fat'].sum()

    macro_data = {
        'Macro': ['Protein', 'Carbs', 'Fat'],
        'Grams': [total_protein, total_carbs, total_fat],
        'Calories': [total_protein * 4, total_carbs * 4, total_fat * 9]
    }
    macro_df = pd.DataFrame(macro_data)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="card">
            <h4>Macro Breakdown</h4>
            <p>💪 Protein: <b>{total_protein:.0f}g</b> ({total_protein*4:.0f} kcal)</p>
            <p>🍞 Carbs: <b>{total_carbs:.0f}g</b> ({total_carbs*4:.0f} kcal)</p>
            <p>🧈 Fat: <b>{total_fat:.0f}g</b> ({total_fat*9:.0f} kcal)</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.bar_chart(macro_df.set_index('Macro')[['Grams']], use_container_width=True)

    st.markdown("---")

    # Food frequency
    st.markdown("### 🥘 Most Logged Foods")
    food_freq = filtered_df['food'].value_counts().head(10)

    if not food_freq.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart(food_freq, use_container_width=True)

        with col2:
            for food, count in food_freq.items():
                total_cals = filtered_df[filtered_df['food'] == food]['calories'].sum()
                st.markdown(f"**{food}** — {count}x ({total_cals} kcal total)")

    st.markdown("---")

    # Summary stats
    st.markdown("### 📊 Summary Statistics")
    col1, col2, col3 = st.columns(3)

    with col1:
        avg_daily_calories = round(total_calories / unique_days) if unique_days > 0 else 0
        st.metric("⌛ Avg Daily Calories", f"{avg_daily_calories} kcal")

    with col2:
        avg_daily_protein = round(total_protein / unique_days, 1) if unique_days > 0 else 0
        st.metric("💪 Avg Daily Protein", f"{avg_daily_protein}g")

    with col3:
        meals_per_day = round(total_meals / unique_days, 1) if unique_days > 0 else 0
        st.metric("🍽️ Meals/Day Avg", f"{meals_per_day}")
