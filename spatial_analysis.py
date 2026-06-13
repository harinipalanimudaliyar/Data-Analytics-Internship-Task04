import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("==================================================")
print(" VIRTUALWORKS LABS - GEOSPATIAL ANALYSIS ENGINE  ")
print("==================================================\n")

# [Step 1] Load your location dataset
print("[1/4] Parsing coordinate logging sheets...")
df = pd.read_csv('location_dataset.csv')

# [Step 2] Calculate Algorithmic Market Gap Score
print("[2/4] Executing spatial density gap algorithms...")
df['market_gap_score'] = df['sales_demand_score'] / (df['existing_stores_count'] + 1)
df = df.sort_values(by='market_gap_score', ascending=False)

# [Step 3] Generate the Polished Geospatial Map
print("[3/4] Running visual coordinate plotting engine...")
plt.figure(figsize=(11, 7))

# Renders bubbles using professional balanced cool-to-warm contrast tones
scatter = plt.scatter(df['longitude'], df['latitude'], 
                      s=df['market_gap_score'] * 9, 
                      c=df['market_gap_score'], 
                      cmap='coolwarm', edgecolor='#333333', alpha=0.85, linewidth=1.2)

# [Step 4] Smart Text Layout Spacing System
print("[4/4] Applying typography collision protection...")
for i, txt in enumerate(df['region_name']):
    if df['market_gap_score'].iloc[i] > 65:  # High-priority focus markers
        # Shifts label coordinates smoothly to the side (+0.25) to avoid overlap
        plt.text(df['longitude'].iloc[i] + 0.25, df['latitude'].iloc[i], 
                 f"{txt}\n(Gap: {df['market_gap_score'].iloc[i]:.1f})", 
                 ha='left', va='center', fontweight='bold', fontsize=8.5,
                 color='#1A237E', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

# Clean up layout formatting styles
plt.title('Geospatial Market Gap Analysis: Business Expansion Hotspots', fontsize=14, fontweight='bold', pad=25)
plt.xlabel('Longitude Coordinates', fontsize=11, fontweight='bold', color='#212121')
plt.ylabel('Latitude Coordinates', fontsize=11, fontweight='bold', color='#212121')
plt.grid(True, linestyle=':', alpha=0.4)

# Dynamic zoom limits so shifted text stays cleanly inside frames
plt.xlim(df['longitude'].min() - 1, df['longitude'].max() + 3)
plt.ylim(df['latitude'].min() - 1, df['latitude'].max() + 1)

# Add clear professional color index bar
cbar = plt.colorbar(scatter, pad=0.03)
cbar.set_label('Expansion Priority Index (Market Gap Scale)', fontsize=10, fontweight='bold')

plt.tight_layout()

# Save the polished visualization asset directly to local folder
plt.savefig('expansion_hotspots_map.png', dpi=300)

# FORCE CHART TO SHOW DIRECTLY ON GOOGLE COLAB CELL SCREEN
plt.show() 

print("\n Run complete! Map has been drawn and saved as 'expansion_hotspots_map.png'")
