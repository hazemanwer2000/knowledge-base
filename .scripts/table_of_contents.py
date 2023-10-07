
import os
import json
import re

# Template for every TOC entry
model_toc_entry = '* [DISPLAY-NAME](#ICONIC-NAME)\n'

# Convert display title to iconic title (e.g: 'The Boy' to 'the-boy')
def iconize_title(name):
    name = re.sub("[^0-9a-zA-Z]", "-", name)
    name = re.sub("-+", "-", name)
    name = re.sub("^-", "", name)
    name = re.sub("-$", "", name)
    name = name.lower()
    return name

# Processes each file
def process_file(file_path):
    # Parse 'JSON'
    with open(file_path, encoding="utf-8") as f:
        parsed = json.loads(f.read())

    # Get all cell(s) with title
    title_cells = [cell for cell in parsed['cells'] if (
        (cell['cell_type'] == 'markdown') and
        (cell['source'][0].startswith(r'#'))
    )]

    # Get TOC cell
    toc_cell = title_cells[1]

    # Create new TOC array
    toc_array = [
        "## Table of Contents\n"
    ]
    
    # Loop on each relevant title cell
    for cell in title_cells[2:]:
        cell['source'][0] = re.sub(" +<a.*</a>", "", cell['source'][0])
        hashtags, name = re.split(r"# +", cell['source'][0])
        depth = len(hashtags) - 1
        iconic_name = iconize_title(name)
        
        # Append '<a>...</a>'
        cell['source'][0] = cell['source'][0] + ' <a class="anchor" id="' + iconic_name + '"></a>'

        # Create TOC entry
        toc_entry = model_toc_entry[:]
        toc_entry = toc_entry.replace("DISPLAY-NAME", name)
        toc_entry = toc_entry.replace("ICONIC-NAME", iconic_name)
        toc_entry = ('  ' * depth) + toc_entry

        # Append TOC entry
        toc_array.append(toc_entry)
    
    # Overwrite TOC
    toc_cell['source'] = toc_array

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

# Note: Depends on the script's path in the repo.
starting_directory = os.path.dirname(os.path.dirname(__file__))

process_directory(starting_directory)