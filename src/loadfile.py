import os

def read_file(relfilepath):
    """Read the contents of a file and return as a string."""
    script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
    script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
    abs_file_path = os.path.join(script_dir, relfilepath)
    with open(abs_file_path, 'r', encoding='utf-8') as f:
        return f.readlines()
    
    
    
