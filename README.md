# ⚽ FIFA23 Player & Team Explorer

Explore official FIFA 23 player and club data with an interactive Streamlit interface.

🔗 **Live App:** [https://fifadeploy.streamlit.app](https://fifadeploy.streamlit.app)

---

## 🧠 About the Project

This project allows you to visualize and analyze FIFA 23 players and teams based on real-world data from Kaggle.  
It was built as a data exploration tool for football enthusiasts, analysts, and students.

**You can:**
- View individual player statistics
- Filter by club and explore attributes like age, position, salary, and market value
- Display club badges, player photos, national flags, and key stats
- Track overall performance using progress bars

---

## Demo
<img width="1841" height="841" alt="image" src="https://github.com/user-attachments/assets/e69f8d55-9392-4952-938c-57f797fa53ae" />
<img width="1848" height="841" alt="image" src="https://github.com/user-attachments/assets/36c7cfdd-88fb-4357-92d3-2aa3d6f693cb" />
<img width="1844" height="831" alt="image" src="https://github.com/user-attachments/assets/2b11486a-5199-4065-8663-4e610e677b3b" />

---
## 📊 Features

### 📌 Home Page
- Introduction to the dataset
- Link to download the original data
- Filters players with valid contracts and non-zero market value

### 🧑‍🎓 Players
- Select a club and see the available players
- Choose a player to display:
  - Photo
  - Age, height, weight
  - Position and overall
  - Market value, weekly wage, and release clause

### 🏟️ Teams
- Select a club and view:
  - Team logo
  - A table with player attributes
  - Progress bars for salary and overall rating

---

## 🗂 Dataset

- **Source:** [FIFA 23 Complete Player Dataset – Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset)
- **Data cleaning includes:**
  - Removed players with expired contracts
  - Removed players with missing market values
  - Sorted by `"Overall"` rating

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/joaoeferrari/streamlit_fifa_deploy.git
cd streamlit_fifa_deploy

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run 1_home.py
