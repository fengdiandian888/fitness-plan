import os

full_path = r'd:\solo\test_write.txt'
print('Full path:', full_path)
print('Parent exists:', os.path.exists(r'd:\solo'))

with open(full_path, 'w') as f:
    f.write('test content')
    
print('Write completed')
print('File exists:', os.path.exists(full_path))
