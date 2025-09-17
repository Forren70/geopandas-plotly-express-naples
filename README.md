# Geopandas Plotly Express Naples

This repository contains a GIS project for Naples, Italy, demonstrating geospatial analysis with **Geopandas**, **Matplotlib**, **Contextily**, and **Plotly Express**. The project includes three Python scripts, geospatial datasets, and generated maps.

## Contents

- `geopandas-plotly-express-naples.py` – Basic map of Naples with parks and hotels
- `geopandas-plotly-express-naples-buffer.py` – Map showing 150m buffer around parks and hotels
- `geopandas-plotly-express-naples-intersected-hotels.py` – Map of hotels within 150m of parks
- `Naples_geopandas/` – Folder containing `.shp` files and the ArcGIS project `.aprx`
- `Screenshots/` – Folder containing map images: `map1.png`, `map2.png`, `map3.png`

## Map Examples

### Map 1: Parks and Hotels in Naples

![Map 1](Screenshots/map1.png)

### Map 2: 150m Buffer Analysis

![Map 2](Screenshots/map2.png)

### Map 3: Suitable Hotels (within 150 m from Parks)

![Map 3](Screenshots/map3.png)

## Dependencies

This project uses the following Python libraries:

- geopandas
- matplotlib
- contextily
- plotly-express

## How to Run the Scripts

1. Make sure all the shapefiles are in the `Naples_geopandas` folder.
2. Place the screenshots folder `Screenshots` in the same repository if you want to view the generated maps.
3. Run the scripts in this order:

   ```bash
   python geopandas-plotly-express-naples.py
   python geopandas-plotly-express-naples-buffer.py
   python geopandas-plotly-express-naples-intersected-hotels.py
