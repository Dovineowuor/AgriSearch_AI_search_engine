import os

# Define the folder and file structure
structure = {
    "backend": [
        "app.py", 
        "models.py", 
        "embeddings.py", 
        "chromadb_client.py", 
        "utils.py"
    ],
    "frontend": {
        "static": {
            "css": ["style.css"],
            "js": ["script.js"]
        },
        "templates": ["index.html"],
        "app.js": []
    },
    "embeddings": [
        "clip.py", 
        "sbert.py", 
        "whisper.py", 
        "vggish.py"
    ],
    "data": {
        "uploads": [],
        "dataset": []
    },
    "": ["config.py", "requirements.txt", "README.md"]
}

# Function to create directories and files
def create_structure(base_path, structure):
    for folder, contents in structure.items():
        folder_path = os.path.join(base_path, folder)
        
        if isinstance(contents, list):  # If contents are a list, they are files
            os.makedirs(folder_path, exist_ok=True)
            for file in contents:
                file_path = os.path.join(folder_path, file)
                if file:  # Create only if file name is provided
                    with open(file_path, 'w') as f:
                        f.write(f"# Placeholder for {file}\n")
        elif isinstance(contents, dict):  # If contents are a dict, it's a folder with subfolders
            os.makedirs(folder_path, exist_ok=True)
            create_structure(folder_path, contents)

# Base path for the project (current directory)
base_path = "."

# Create the folder structure
create_structure(base_path, structure)

print("Project structure created successfully!")
