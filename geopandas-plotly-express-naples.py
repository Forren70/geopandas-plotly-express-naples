import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

# --- 1. Define parameters and load data ---
SHP_DIR = "Naples_geopandas/"
HOTELS_FILE = SHP_DIR + "Naples_Hotels_32633.shp"
PARKS_FILE = SHP_DIR + "Naples_Parks_32633.shp"
BOUNDARY_FILE = SHP_DIR + "Naples_boundaries_Dissolve.shp"

# Common visualization styles
BOUNDARY_STYLE = {'facecolor': 'none', 'edgecolor': 'darkblue', 'linewidth': 1.5}
PARKS_STYLE = {'facecolor': 'green', 'edgecolor': 'black', 'alpha': 0.3}
HOTELS_ALL_STYLE = {'marker': 'o', 'color': 'red', 'markersize': 5}

# Load data with error handling
try:
    hotels = gpd.read_file(HOTELS_FILE)
    parks = gpd.read_file(PARKS_FILE)
    naples_boundary = gpd.read_file(BOUNDARY_FILE)
except FileNotFoundError as e:
    print(f"Error: could not find a file. Check the path: {e}")
    exit()

# Pre-processing and reprojecting for visualization (Web Mercator)
hotels_wm = hotels.to_crs(epsg=3857)
parks_wm = parks.to_crs(epsg=3857)
naples_boundary_wm = naples_boundary.to_crs(epsg=3857)

# --- Function to add common map elements ---
def add_common_elements(fig, ax, title, legend_handles):
    """Adds basemap, title, legend, and North arrow."""
    ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
    ax.set_title(title, fontsize=16, pad=10)
    ax.legend(handles=legend_handles, loc='upper left', frameon=True, shadow=True)

    # North arrow
    ax.text(0.9, 0.95, 'N', transform=ax.transAxes, fontsize=14, fontweight='bold', ha='center', va='center')
    arrow = FancyArrowPatch(
        (0.9, 0.91), (0.9, 0.94),
        transform=ax.transAxes,
        arrowstyle='-|>,head_width=6,head_length=8',
        color='black', linewidth=1.5
    )
    ax.add_patch(arrow)
    ax.set_axis_off()
    fig.tight_layout()

# --- 2. Map 1: Base Map (Parks and All Hotels) ---
fig1, ax1 = plt.subplots(1, 1, figsize=(10, 10))
naples_boundary_wm.plot(ax=ax1, **BOUNDARY_STYLE)
parks_wm.plot(ax=ax1, **PARKS_STYLE)
hotels_wm.plot(ax=ax1, **HOTELS_ALL_STYLE)

# Legend for Map 1
legend_handles1 = [
    mpatches.Patch(facecolor='none', edgecolor='darkblue', linewidth=1.5, label='Naples Boundary'),
    mpatches.Patch(facecolor='green', alpha=0.3, label='Parks'),
    plt.Line2D([], [], label='All Hotels', **HOTELS_ALL_STYLE, linestyle='None')
]

add_common_elements(fig1, ax1, 'Map 1: Parks and All Hotels in Naples', legend_handles1)

# Save figure
fig1.savefig("Screenshots/map1.png", dpi=300)
plt.show()







