\# 🏟️ Marvel Stadium Attendance Predictor



> \*"I work at Marvel Stadium as a Food \& Beverage Attendant. I wanted to know — 

> what actually drives a busy day? I built a machine learning model to find out."\*



\## 📌 Project Overview

A machine learning project that predicts high-traffic days at Marvel Stadium 

using real event data, weather conditions and AFL match records.



Built as part of my analytics portfolio to demonstrate end-to-end data science 

skills — from data collection through to a live interactive web application.



\---



\## 🔍 Key Findings

\- \*\*Day of week\*\* is the single strongest predictor of busy days — accounting for \*\*55%\*\* of the model's decisions

\- \*\*Saturday games\*\* dominate with 63 games vs zero on Mon/Tue/Wed

\- \*\*July is the busiest month\*\* — AFL finals season drives a massive spike

\- Weather (rain, temperature) has surprisingly \*\*little impact\*\* on attendance patterns

\- Both Logistic Regression and Random Forest achieved \*\*100% accuracy\*\* on test data



\---



\## 📊 Data Sources

| Dataset | Source | Records |

|---|---|---|

| Event listings | Ticketmaster Discovery API | 82 events |

| Weather data | Open-Meteo API (free, no key needed) | 1,096 days |

| AFL match records | AFL Tables (afltables.com) | 150 Marvel Stadium games (2022-2024) |

| Public holidays | Nager.at Public Holidays API | 76 holidays |



\---



\## 🛠️ Tech Stack

\- \*\*Python\*\* — pandas, scikit-learn, matplotlib, seaborn

\- \*\*Machine Learning\*\* — Logistic Regression, Random Forest Classifier

\- \*\*Web App\*\* — Streamlit

\- \*\*APIs\*\* — Ticketmaster, Open-Meteo, AFL Tables, Nager.at



\---



\## 📁 Project Structure

Marvel\_Stadium\_Project/

├── data/                          # All datasets and charts

├── 01\_data\_collection.ipynb       # API data collection

├── 02\_data\_cleaning\_eda.ipynb     # Cleaning + exploratory analysis

├── 03\_feature\_engineering.ipynb   # Feature creation

├── 04\_modelling.ipynb             # ML model training + evaluation

└── app.py                         # Streamlit web application



\---



\## 🚀 How to Run

```bash

\# Clone the repo

git clone https://github.com/yourusername/Marvel\_Stadium\_Project



\# Install dependencies

pip install requests pandas scikit-learn streamlit matplotlib seaborn joblib



\# Run the app

streamlit run app.py

```



\---



\## 📈 Model Performance

| Model | Accuracy | F1 Score |

|---|---|---|

| Logistic Regression | 100% | 1.00 |

| Random Forest | 100% | 1.00 |



High accuracy reflects strong feature engineering — day of week and weekend 

flags are near-perfect predictors of high-traffic days at a sports venue.



\---



\## 👩‍💻 About

\*\*Venissa Dsouza\*\* — Master of Analytics student at RMIT University, Melbourne  

Background in AI \& Machine Learning (BE) | Python · R · Power BI · Tableau



\[!\[LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/venissa-dsouza-829552217)

