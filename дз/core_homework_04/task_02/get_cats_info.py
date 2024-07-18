from pathlib import Path

def get_cats_info(path):
    cats_info = []
    
    with open(path, "r") as file:
        for line in file.readlines():
            cat_info = {}
            cat_info.update({"id": str(line.split(',')[0].strip()), "name": str(line.split(',')[1].strip()), "age": str(line.split(',')[2].strip())})
            cats_info.append(cat_info)
    
    return cats_info

current_dir = Path(__file__).parent
# relative_path = current_dir / "Cats.txt"

# cats_info = get_cats_info(relative_path)
# print(cats_info)