# 🎣 Fishing Fleet Tracker

An interactive data analysis and visualization dashboard for the **Monthly Fishing Fleet 2024** dataset provided by [Global Fishing Watch](https://globalfishingwatch.org/).

---

## 📖 About

This project analyzes fishing vessel activity across the world's oceans using AIS (Automatic Identification System) data. The dashboard allows users to explore vessel distributions, fishing activity patterns, gear types, and geographic hotspots through interactive charts and a 3D globe visualization.

The dataset contains information about:
- Fishing vessel identifiers (MMSI)
- Month of observation
- Geographic location (latitude & longitude)
- Country of origin (flag)
- Gear type used for fishing
- Time spent on water
- Loitering activity
- Number of vessels present

---

## 🚀 Features

- **Vessel Distribution** — Pie chart of the top 19 countries by total vessel count
- **Country-wise Activity** — Breakdown of loitering vs non-loitering vessels per country
- **Gear Type Distribution** — Top gear types used by a selected country
- **3D Globe Visualization** — Interactive globe showing vessel density by location using column layers (powered by PyDeck)
- **Flexible Filtering** — Filter data by country, gear type, activity type (loitering / non-loitering / both), and month

---

## 🗂️ Project Structure

```
Mmsi_fleet/
│
├── Datasets/
│   └── combined_dataset.csv       # Merged monthly fishing fleet data
│
├── functions.py                   # All data processing and visualization logic
├── app.py                  # Streamlit app UI
├── data_transformation.ipynb      # Data cleaning and merging notebook
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/Neer-17/Mmsi_fleet.git
cd Mmsi_fleet
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```

---

## 📊 Dataset

- **Source:** [Global Fishing Watch](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort)
- **Name:** Monthly Fishing Fleet 2024
- **Coverage:** Global, monthly resolution
- **Key Columns:** `mmsi_present`, `flag`, `geartype`, `lat`, `lon`, `loitering`, `month`

---

## 🌍 Visualizations

### Pie Charts (Plotly)
Available for three views selectable via dropdown:
- Vessel distribution by country
- Loitering vs non-loitering activity by country
- Gear type breakdown by country

### 3D Globe (PyDeck + GlobeView)
Displays vessel density as 3D columns on an interactive globe. Each column's height represents the number of vessels (`mmsi_present`) at that location. Rendered using `streamlit.components.v1.html()` to support PyDeck's `_GlobeView` which is not natively supported by `st.pydeck_chart()`.

---

## 🔍 Key Functions (`functions.py`)

| Function | Description |
|---|---|
| `country_dis()` | Returns vessel counts grouped by country (top 19 + Other) |
| `activity_dis(country)` | Returns loitering vs non-loitering split for a country |
| `geartype_dis(country)` | Returns top 5 gear types used by a country |
| `get_data(country, gtype, activity, month)` | Filters the dataset based on selected parameters |
| `globe_plot(data)` | Returns a PyDeck Deck object with GlobeView and ColumnLayer |

---

## 📝 Notes

- Selecting `ALL` as the country in the globe view is disabled due to dataset size — filter by a specific country for globe rendering.
- The globe visualization requires an active internet connection to load the GeoJSON base map from the [Natural Earth CDN](https://d2ad6b4ur7yvpq.cloudfront.net/).

---

## 📄 License

This project uses data provided by [Global Fishing Watch](https://globalfishingwatch.org/) under their open data license. Please refer to their website for data usage terms.

---

## 🙋 Author

**Neer-17** — [GitHub Profile](https://github.com/Neer-17)
