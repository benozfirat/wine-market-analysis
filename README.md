

# 🍷 Wine Market Analysis
<p align="center">
  <a href="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1">
      <img src="https://media.wired.com/photos/641337bd5e3ab3be4fe3e789/master/w_1600%2Cc_limit/sql_normal.gif" alt="Click me !" width="500" />
  </a>
</p>

## Language
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org) [![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org) [![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/) [![StreamLit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

## 📝 Description

**The Wiwino Market** Analysis project, conducted as part of the **BeCode** training, focuses on analyzing the wine market using specific skills. Data Engineers enhance their **SQL skills** to query and extract relevant wine data, such as top-selling wines and customer preferences. Meanwhile, Data Analysts use **Streamlit** to create interactive visualizations based on this data, providing clear and actionable insights into wine market trends. Task management is organized through **Trello** to ensure effective and structured collaboration throughout the project.

## 📚 Table of Contents
- [📝 Description](#-description)
- [💻 Installation](#-installation)
- [🏃‍♂️ How to Run](#-How-to-Run)
- [🎓 Team Members](#-Team-Members)
- [📂 Project Structure](#-project-structure)

## 💻 Installation

```bash
git clone git@github.com:benozfirat/wine-market-analysis.git
cd wine-market-analysis
pip install -r requirements.txt
```
## 🏃‍♂️ How to Run

```bash
python main.py
```

## 🎓 Team Members

- **👷‍♂️ [Atome1212](https://github.com/Atome1212)**: Data Engineer
- **👷‍♂️ [Jojopanis](https://github.com/Jojopanis)**: Data Engineer
- **👨‍💻 [benozfirat](https://github.com/benozfirat)**: Data Analyst
- **👩‍💻 [EmmaSHANG0625](https://github.com/EmmaSHANG0625)** : Data Analyst

## 📂 Project Structure

```bash 

├── .gitignore
├── README.md
├── Streamlit_App
│   ├── Vivino.py
│   ├── get_results.py
│   └── pages
│       ├── 10_💸_BigBudgetRecommandations.py
│       ├── 1_📈_Top10.py
│       ├── 2_🎯_TargetCountries.py
│       ├── 3_🏆_Awards.py
│       ├── 4_👅_SpecificTastes.py
│       ├── 5_🍇_MostAccessibleWines.py
│       ├── 6_🥇_CountriesLeaderboard.py
│       ├── 7_💎_VIPSelection.py
│       ├── 8_🌳_NaturalWines.py
│       └── 9_⚗️_SecretPotion.py
├── assets
│   └── vivino_db_diagram_horizontal.png
├── csv
│   ├── bq1_natural
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── bq2_match_keyword
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q1_csv_most_popular
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q2_countries
│   │   ├── countries.csv
│   │   └── script.py
│   ├── q3_GEPETTO
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q3_Toxic_award_CSV
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q3_best_vintage
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q3_sweetness
│   │   ├── script.py
│   │   └── sweetness_index.csv
│   ├── q4_keyword
│   │   ├── code.py
│   │   ├── info.txt
│   │   └── wines_data.csv
│   ├── q5_most_wines
│   │   ├── script.py
│   │   ├── wines_count.csv
│   │   └── wines_ratings.csv
│   ├── q6_average_rating
│   │   ├── rating_per_countries.csv
│   │   └── script.py
│   └── q7_one_of_our_VIP
│       ├── code.py
│       ├── info.txt
│       └── wines_data.csv
├── db
│   └── vivino.db
├── requirements.txt
└── utils
    ├── Acidity.csv
    ├── Best_vintage_winery.csv
    ├── Cabernet_Sauvignon.csv
    ├── Geppetto_Award.csv
    ├── Natural_Wines.csv
    ├── Secret_Potion.csv
    ├── Specific_Taste.csv
    ├── countries.csv
    ├── grapes_count.csv
    ├── images
    │   ├── Dalton.jpg
    │   ├── Geppetto_Pinocchio.jpeg
    │   ├── Mr.Geppetto.jpeg
    │   └── Vivino.png
    ├── rating_per_countries.csv
    ├── wines_data.csv
    └── wines_ratings.csv
```
This tree provides an overview of the project structure, showing where each file and directory is located.
  
