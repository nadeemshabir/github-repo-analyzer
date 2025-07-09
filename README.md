# GitHub Repo Analyzer
A Python project that fetches, analyzes, and visualizes data from GitHub repositories. Designed to help developers and researchers extract useful insights like stars, forks, activity, and popularity of repositories.

____
## 📌 Features

- ✅ Fetch GitHub repo data via API
- 📊 Visualize metrics like stars, forks, issues, etc.
- 🧠 Score repositories based on custom logic
- 🖥️ Simple `app.py` to run the full pipeline

___
## Project Structure
github-repo-analyzer/
├── app.py # Main script to run the full pipeline
├── fetchingdata.py # Fetches repo data from GitHub API
├── visualization.py # Handles all visualizations
├── scoring.py # Applies custom scoring logic
├── github_repos.csv # Output CSV of fetched data
├── .gitignore # Specifies untracked files (pycache)
├── README.md # You're here!

___
## How it Works?
1. **Fetching Data**:  
   `fetchingdata.py` uses the GitHub API to get data for repositories listed.

2. **Scoring Repos**:  
   `scoring.py` assigns a score to each repo based on custom criteria (e.g., stars, forks, open issues).

3. **Visualizing Results**:  
   `visualization.py` creates charts to analyze popularity, activity, etc.

4. **Running the App**:
   in the terminal of 'app.py' run 'streamlit run app.py'
