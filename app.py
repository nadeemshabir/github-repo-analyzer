import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scoring import compute_health_score  # Make sure this function exists

st.set_page_config(page_title="GitHub Repo Analyzer", layout="wide")

st.title("📊 GitHub Repo Analyzer")
st.markdown("Analyze and visualize the health of GitHub repositories with customizable weights.")

# Sidebar: Upload CSV or use default
st.sidebar.header("📂 Data Source")
uploaded_file = st.sidebar.file_uploader("Upload a GitHub CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Custom file uploaded successfully!")
else:
    df = pd.read_csv('github_repos.csv')
    st.info("ℹ️ Using default dataset: `github_repos.csv`")

# Sidebar: Weight sliders
st.sidebar.header("⚙️ Weight Configuration")
star_weight = st.sidebar.slider("Weight for Stars ⭐", 0.0, 1.0, 0.4, help="Stars indicate popularity")
fork_weight = st.sidebar.slider("Weight for Forks 🍴", 0.0, 1.0, 0.2, help="Forks show community interest")
contrib_weight = st.sidebar.slider("Weight for Contributors 👥", 0.0, 1.0, 0.2, help="Contributors show collaboration")
watch_weight = st.sidebar.slider("Weight for Watchers 👀", 0.0, 1.0, 0.2, help="Watchers reflect user engagement")

weights = {
    'Stars': star_weight,
    'Forks': fork_weight,
    'Contributors': contrib_weight,
    'Watchers': watch_weight
}

# Normalize weights
total_weight = sum(weights.values())
if total_weight > 0:
    weights = {k: v / total_weight for k, v in weights.items()}
else:
    st.error("Total weight cannot be zero. Please adjust the sliders.")
    st.stop()

# Compute health scores
df = compute_health_score(df, weights)

# Sort order toggle
st.sidebar.header("🔽 Sorting")
sort_order = st.sidebar.radio("Sort Top Repositories", ["Descending", "Ascending"], index=0)
ascending = sort_order == "Ascending"

# Top 10 repos
top_repos = df.sort_values(by='Health_Score', ascending=ascending).head(10)

# Show table
st.subheader("🏆 Top 10 Repositories by Health Score")
st.dataframe(top_repos[['Name', 'Health_Score']].reset_index(drop=True))

# Plot chart
st.subheader("📈 Health Score Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_repos['Name'], top_repos['Health_Score'], color='skyblue')
ax.set_xlabel("Health Score")
ax.set_title("Top 10 GitHub Repositories")
ax.invert_yaxis()
plt.tight_layout()
st.pyplot(fig)
