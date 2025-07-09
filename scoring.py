import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('github_repos.csv')

# Health score computation function
def compute_health_score(df, weights):
    """
    Compute a health score for each repository based on normalized metrics and weights.
    """
    for metric in weights:
        max_val = df[metric].max()
        df[f'norm_{metric}'] = df[metric] / max_val if max_val > 0 else 0
        
    df['Health_Score'] = sum(df[f'norm_{metric}'] * w for metric, w in weights.items())
    return df

# Weight settings (can be changed or made dynamic)
weights = {
    'Stars': 0.4,
    'Forks': 0.2,
    'Contributors': 0.2,
    'Watchers': 0.2
}

# Compute scores
df = compute_health_score(df, weights)

# Select top 10 by score
top_repos = df.sort_values(by='Health_Score', ascending=False).head(10)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_repos['Name'], top_repos['Health_Score'], color='skyblue')
plt.xlabel('Health Score')
plt.title('Top 10 Repositories by Health Score')
plt.gca().invert_yaxis()  # Show highest score on top
plt.tight_layout()
plt.show()
