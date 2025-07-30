# 📍 Geolocation Filter and Visualization Tool

This project processes a list of Google Maps URLs containing GPS coordinates. It extracts the coordinates, selects at least 50 locations that are **500 meters apart**, and generates JavaScript code to **visualize them on a map** using [Leaflet.js](https://leafletjs.com/).

---

## 🧠 Features

- 📌 Extracts latitude and longitude from raw Google Maps URLs.
- 📏 Calculates distances between points using the **Haversine formula**.
- 🚫 Filters out points that are too close to each other (closer than 500 meters).
- ⚙️ Outputs:
  - A JavaScript object of selected coordinates
  - A list of coordinate pairs with distances ≥ 500m for drawing red lines
- 🗺️ Ready-to-use with Leaflet for interactive visualization.

---

## 🛠️ How It Works

1. **Extract Coordinates:**
   - Uses regular expressions to parse URLs and extract latitude & longitude.

2. **Haversine Distance Calculation:**
   - Implements the Haversine formula to compute distances between two coordinates on Earth.

3. **Filtering Logic:**
   - Iterates through the points and only selects those that are at least 500 meters apart from already-selected points.
   - Stops when it has selected 50 valid locations.

4. **Ja**
