import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# --- 1. Load GeoDataFrames from Shapefiles ---
hotels = gpd.read_file("Naples_geopandas/Naples_Hotels_32633.shp")
parks = gpd.read_file("Naples_geopandas/Naples_Parks_32633.shp")
naples_boundary = gpd.read_file("Naples_geopandas/Naples_boundaries_Dissolve.shp")

# --- 2. Create figure and axis ---
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# --- 3. Reproject to Web Mercator for contextily ---
hotels_wm = hotels.to_crs(epsg=3857)
parks_wm = parks.to_crs(epsg=3857)
naples_boundary_wm = naples_boundary.to_crs(epsg=3857)

# --- 4. Create 150-meter buffer around parks ---
# Buffer calculation on metric CRS (EPSG:32633)
parks_buffer = parks.buffer(150)
parks_buffer_gdf = gpd.GeoDataFrame(geometry=parks_buffer, crs=parks.crs)

# Optional: save buffer shapefile
parks_buffer_gdf.to_file("Naples_geopandas/parks_buffer_150m.shp")

# Reproject buffer for plotting
parks_buffer_wm = parks_buffer_gdf.to_crs(epsg=3857)

# --- 5. Plot layers ---
naples_boundary_wm.plot(ax=ax, facecolor='none', edgecolor='darkblue', linewidth=1, label='Naples Boundary')
parks_wm.plot(ax=ax, color='green', edgecolor='black', alpha=0.3, label='Parks')
parks_buffer_wm.plot(ax=ax, color='blue', alpha=0.3, edgecolor='none', label='150m Parks Buffer')
hotels_wm.plot(ax=ax, marker='o', color='red', markersize=5, label='Hotels')

# Add basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# --- 6. Legend handles ---
boundary_patch = mpatches.Patch(facecolor='none', edgecolor='darkblue', linewidth=1.5, label='Naples Boundary')
parks_patch = mpatches.Patch(color='green', alpha=0.3, label='Parks')
buffer_patch = mpatches.Patch(color='blue', alpha=0.3, label='150m Parks Buffer')
hotels_point = plt.Line2D([], [], marker='o', color='red', markersize=5, linestyle='None', label='Hotels')

ax.legend(handles=[boundary_patch, parks_patch, buffer_patch, hotels_point], loc='upper left')

# --- 7. Add North Arrow ---
ax.text(0.9, 0.95, 'N', transform=ax.transAxes, fontsize=16, fontweight='bold', ha='center', va='center')
arrow = FancyArrowPatch((0.9, 0.91), (0.9, 0.94), transform=ax.transAxes, arrowstyle='-|>,head_width=6,head_length=8', color='black', linewidth=2)
ax.add_patch(arrow)

# --- 8. Turn off axes and add title ---
ax.set_axis_off()
ax.set_title("Map 2: 100 m Buffer Analysis", fontsize=16, pad=10)

# --- 9. Save figure ---
fig.savefig("Screenshots/map 2.png", dpi=300)

# --- 10. Display plot ---
plt.show()

