import os
import sys

print(f'Python version: {sys.version}')
print(f'Current directory: {os.getcwd()}')
print(f'Running from: {__file__}')
print(f'Parent directory exists: {os.path.exists(os.path.dirname(__file__))}')

full_path = os.path.join(os.path.dirname(__file__), 'test_write3.txt')
print(f'Full path: {full_path}')

try:
    with open(full_path, 'w') as f:
        f.write('test content')
    print('Write succeeded')
    print(f'File exists after write: {os.path.exists(full_path)}')
    if os.path.exists(full_path):
        print(f'File size: {os.path.getsize(full_path)} bytes')
except Exception as e:
    print(f'Error: {e}')
