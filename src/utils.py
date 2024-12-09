
import os
import sys

def is_file_valid(file):
    if not os.path.isfile(file):
        return False, f'Error: File {file} does not exist!'
    
    if not os.access(file, os.R_OK):
        return False, f'Error: File {file} does not have read permission'
    
    if not file.lower().endswith('.txt'):
        return False, f'Error: allowed extensions: \'.txt\''
    
    return True, None

def create_or_replace_file_with_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)