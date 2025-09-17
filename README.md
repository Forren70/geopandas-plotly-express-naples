# Geopandas Plotly Express Naples

This repository contains a GIS project for Naples, Italy, showcasing geospatial analysis using **Geopandas**, **Matplotlib**, **Contextily**, and **Plotly Express**. The project includes:  

- A point shapefile of the main hotels in Naples.  
- A polygon shapefile of the main urban parks in Naples.  
- Map 1: a basic map showing all hotels and parks.  
- Map 2: a 150-meter buffer around parks, visualizing all hotels in relation to this buffer.  
- Map 3: the intersection showing “suitable hotels” (4 hotels in total) located within 150 meters of a park, ideal for visitors seeking accommodation close to green urban areas.  
- Three Python scripts to generate these maps.  
- All geospatial datasets and generated map images.  

## Contents

- `geopandas-plotly-express-naples.py` – Basic map of Naples with parks and hotels
- `geopandas-plotly-express-naples-buffer.py` – Map showing 150m buffer around parks and hotels
- `geopandas-plotly-express-naples-intersected-hotels.py` – Map of hotels within 150m of parks
- `Naples_geopandas/` – Folder containing `.shp` files and the ArcGIS project `.aprx`
- `screenshots/` – Folder containing map images: `map 1.png`, `map 2.png`, `map 3.png`

## Map Examples

### Map 1: Parks and Hotels in Naples

![Map 1](screenshots/map%201.png)

### Map 2: 150m Buffer Analysis

![Map 2](screenshots/map%202.png)

### Map 3: Suitable Hotels (within 150 m from Parks)

![Map 3](screenshots/map%203.png)

## Dependencies

This project uses the following Python libraries:

- geopandas
- matplotlib
- contextily
- plotly-express

## How to Run the Scripts

1. Make sure all the shapefiles are in the `Naples_geopandas` folder.
2. Place the `screenshots` folder in the same repository if you want to view the generated maps.
3. Run the scripts in this order:

```bash
python geopandas-plotly-express-naples.py
python geopandas-plotly-express-naples-buffer.py
python geopandas-plotly-express-naples-intersected-hotels.py

