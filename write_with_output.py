import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'final_test.txt')

with open(output_path, 'w') as f:
    f.write(f'Script directory: {script_dir}\n')
    f.write(f'Current working directory: {os.getcwd()}\n')
    f.write(f'Creating file...\n')
    
with open(output_path, 'a') as f:
    f.write(f'File exists: {os.path.exists(output_path)}\n')
    f.write(f'File size: {os.path.getsize(output_path) if os.path.exists(output_path) else 0}\n')
