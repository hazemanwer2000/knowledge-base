
import automatey.OS.FileUtils as FileUtils
import automatey.OS.ProcessUtils as ProcessUtils
import automatey.Formats.JSON as JSON
import automatey.Utils.StringUtils as StringUtils

import re

from pprint import pprint

f_jupyterDir = FileUtils.File(__file__).traverseDirectory('../..')
f_jupyterList = f_jupyterDir.listDirectory(isRecursive=True, conditional=lambda x: x.getExtension() == 'ipynb')

class Constants:

    # Template for every TOC entry.
    model_toc_entry = '* [DISPLAY-NAME](#ICONIC-NAME)\n'

def iconizeTitle(name):
    '''
    Convert display title to iconic title (e.g: 'The Boy' to 'the-boy').
    '''
    name = StringUtils.Regex.replaceAll("[^0-9a-zA-Z]", "-", name)
    name = StringUtils.Regex.replaceAll("-+", "-", name)
    name = StringUtils.Regex.replaceAll("^-", "", name)
    name = StringUtils.Regex.replaceAll("-$", "", name)
    name = name.lower()
    return name

for f_jupyter in f_jupyterList:

    jupyter = JSON.fromFile(f_jupyter)

    # Get all cell(s) with title.
    title_cells = [cell for cell in jupyter['cells'] if (
        (cell['cell_type'] == 'markdown') and
        (cell['source'][0].startswith(r'#'))
    )]

    # Get TOC cell.
    toc_cell = title_cells[1]

    # Create new TOC array.
    toc_array = [
        "## Table of Contents\n"
    ]
    
    # Loop on each relevant title cell.
    for cell in title_cells[2:]:
        cell['source'][0] = StringUtils.Regex.replaceAll("<a.*</a>", "", cell['source'][0])
        cell['source'][0] = cell['source'][0].strip()
        hashtags, name = re.split(r"# +", cell['source'][0])
        depth = len(hashtags) - 1
        iconic_name = iconizeTitle(name)
        
        # Append '<a>...</a>'.
        cell['source'][0] = cell['source'][0] + ' <a class="anchor" id="' + iconic_name + '"></a>'

        # Create TOC entry.
        toc_entry = Constants.model_toc_entry[:]
        toc_entry = toc_entry.replace("DISPLAY-NAME", name)
        toc_entry = toc_entry.replace("ICONIC-NAME", iconic_name)
        toc_entry = ('  ' * depth) + toc_entry

        # Append TOC entry.
        toc_array.append(toc_entry)
    
    # Overwrite TOC.
    toc_cell['source'] = toc_array

    FileUtils.File.Utils.recycle(f_jupyter)
    JSON.saveAs(jupyter, f_jupyter, indent=1)
