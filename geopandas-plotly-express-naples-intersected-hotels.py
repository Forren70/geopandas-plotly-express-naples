import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# --- Read the GeoDataFrames from the Shapefiles ---
hotels = gpd.read_file("Naples_geopandas/Naples_Hotels_32633.shp")
parks = gpd.read_file("Naples_geopandas/Naples_Parks_32633.shp")
naples_boundary = gpd.read_file("Naples_geopandas/Naples_boundaries_Dissolve.shp")

# --- Create a figure and a subplot ---
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# --- Reproject to Web Mercator for plotting with contextily ---
hotels_wm = hotels.to_crs(epsg=3857)
parks_wm = parks.to_crs(epsg=3857)
naples_boundary_wm = naples_boundary.to_crs(epsg=3857)

# --- Buffer and intersection ---
# Create a 150-meter buffer around parks in metric CRS (EPSG:32633)
parks_buffer = parks.buffer(150)
parks_buffer_gdf = gpd.GeoDataFrame(geometry=parks_buffer, crs=parks.crs)
parks_buffer_wm = parks_buffer_gdf.to_crs(epsg=3857)

# Spatial join to find hotels within the buffer
intersected_hotels = gpd.sjoin(hotels, parks_buffer_gdf, how="inner", predicate="within")
intersected_hotels_wm = intersected_hotels.to_crs(epsg=3857)

# --- Plot the layers ---
naples_boundary_wm.plot(ax=ax, facecolor='none', edgecolor='darkblue', linewidth=1, label='Naples Boundary')
parks_wm.plot(ax=ax, color='green', edgecolor='black', alpha=0.3, label='Parks')
parks_buffer_wm.plot(ax=ax, color='blue', alpha=0.2, edgecolor='none', label='150m Parks Buffer')

# Plot only intersected hotels with bright green, larger markers
intersected_hotels_wm.plot(ax=ax, marker='o', color='#32CD32', markersize=12, label='Hotels within 150m of a Park')

# --- Add basemap ---
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# --- Create manual legend handles ---
boundary_patch = mpatches.Patch(facecolor='none', edgecolor='darkblue', linewidth=1.5, label='Naples Boundary')
parks_patch = mpatches.Patch(color='green', alpha=0.3, label='Parks')
buffer_patch = mpatches.Patch(color='blue', alpha=0.2, label='150m Parks Buffer')
intersected_hotels_point = plt.Line2D([], [], marker='o', color='#32CD32', markersize=12, linestyle='None', label='Hotels within 150m of a Park')

# Add legend
ax.legend(handles=[boundary_patch, parks_patch, buffer_patch, intersected_hotels_point], loc='upper left')

# --- North arrow ---
ax.text(0.9, 0.95, 'N', transform=ax.transAxes, fontsize=16, fontweight='bold', ha='center', va='center')
arrow = FancyArrowPatch((0.9, 0.91), (0.9, 0.94), transform=ax.transAxes,
                        arrowstyle='-|>,head_width=6,head_length=8', color='black', linewidth=2)
ax.add_patch(arrow)

# Turn off axes
ax.set_axis_off()

# --- Set title and save the figure ---
ax.set_title("Map 3: Suitable Hotels (within 150 m from parks)", fontsize=16, pad=10)
plt.savefig("Screenshots/map 3.png", dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
