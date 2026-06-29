import os

print('Current working directory:', os.getcwd())
print('Files in directory:', os.listdir('.'))
print('Test write...')

with open('test_write.txt', 'w') as f:
    f.write('test')
    
print('Test write completed')
print('Test file exists:', os.path.exists('test_write.txt'))

if os.path.exists('test_write.txt'):
    os.remove('test_write.txt')
    print('Test file removed')
