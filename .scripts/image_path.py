
import os
import json
import re

# Note: Depends on the script's path in the repo.
repo_dir = os.path.dirname(os.path.dirname(__file__))

# Capture image name
def capture_img_name(html_tag):
    src_content = re.findall('src="(.*?)"', html_tag)[0]
    file_name = src_content.split('/')[-1]
    return file_name

# Replace image path
def replace_img_path(html_tag, path):
    compiled = re.compile(r'src=".*?"')
    return compiled.sub('src="' + path + '"', html_tag)

# Get depth of '.ipynb' file
def get_depth_of_file(file_path):
    depth = -1
    while (file_path != repo_dir):
        depth += 1
        file_path = os.path.dirname(file_path)
    return depth

# Processes each file
def process_file(file_path):
    # Parse 'JSON'
    with open(file_path, encoding="utf-8") as f:
        parsed = json.loads(f.read())

    # Get all cell(s) with title
    img_cells = [cell for cell in parsed['cells'] if (
        (cell['cell_type'] == 'markdown') and
        (re.search(r'<img.*/>', cell['source'][0]) != None)
    )]
    
    # Loop on each relevant title cell
    for cell in img_cells:
        img_name = capture_img_name(cell['source'][0])
        depth = get_depth_of_file(file_path)
        proper_path = ('../' * depth) + '.img/' + img_name
        cell['source'][0] = replace_img_path(cell['source'][0], proper_path)

    # Write 'JSON' back to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(parsed, indent=1))

# Iterate all '.ipynb' files, and invoke 'process_file' onto.
def process_directory(directory):
    for root, direcs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file)[1] == '.ipynb':
                process_file(file_path)

process_directory(repo_dir)