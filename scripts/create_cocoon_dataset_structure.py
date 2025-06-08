import os

# Define folder structure
folders = [
    "cocoon_dataset/images/raw",
    "cocoon_dataset/images/processed",
    "cocoon_dataset/images/annotated",
    "cocoon_dataset/data",
    "cocoon_dataset/notebooks",
    "cocoon_dataset/scripts",
    "cocoon_dataset/docs",
    "cocoon_dataset/config"
]

# Create folders and placeholder files
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Add a .gitkeep file to ensure folder is tracked if empty
    with open(os.path.join(folder, ".gitkeep"), "w") as f:
        pass

# Create example files
readme_path = "cocoon_dataset/docs/README.md"
with open(readme_path, "w") as f:
    f.write("# Cocoon Dataset\n\nThis dataset includes cocoon metadata and images for research purposes.\n")

data_dict_path = "cocoon_dataset/docs/data_dictionary.md"
with open(data_dict_path, "w") as f:
    f.write("## Data Dictionary\n\n- Sample_ID: Unique identifier\n- Weight: In grams\n- Length, Width: In mm\n...")

config_path = "cocoon_dataset/config/paths.yaml"
with open(config_path, "w") as f:
    f.write("image_dir: images/processed/\ndata_file: data/cocoon_metadata.csv\n")

print("✅ Cocoon dataset folder structure created successfully.")