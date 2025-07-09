import matplotlib.pyplot as plt
import pandas as pd
df =pd.read_csv('github_repos.csv')
print(df.head())

df = df.dropna(subset=["Name", "Stars"])
# sorting this top 10 starred repos
top= df.sort_values(by="Stars", ascending= False).head(10)
plt.figure(figsize=(10,6))
# plt.bar(top["Name"], top["Stars"], color='orange')
# plt.xticks(rotation=90)
plt.barh(top["Name"], top["Stars"], color='orange')
plt.xlabel('no. of stars')
plt.ylabel('repository name')
plt.title('top 10 stars')

plt.gca().invert_yaxis()  # keeps the most starred at the top
plt.tight_layout()  #fits the things so that the whole graph adjusts on the screen

plt.show() 


# 2. Pie Chart - Language Distribution
language_counts = df["Language"].value_counts().head(6)
plt.figure(figsize=(7, 7))
plt.pie(language_counts, labels=language_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 6 Languages Used")
plt.show()


# 3. Line Plot - Repositories vs Watchers
df_sorted = df.sort_values(by="Watchers", ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.plot(df_sorted["Name"], df_sorted["Watchers"], marker='o', linestyle='-', color='green')
plt.xticks(rotation=45, ha='right')
plt.title("Watchers per Repository")
plt.xlabel("Repository Name")
plt.ylabel("Watchers")
plt.tight_layout()
plt.show()

# 4. Horizontal Bar Chart - Forks per Repository
top_forks = df.sort_values(by="Forks", ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_forks["Name"], top_forks["Forks"], color='orange')
plt.title("Top 10 Repositories by Forks")
plt.xlabel("Forks")
plt.ylabel("Repository Name")
plt.tight_layout()
plt.show()


