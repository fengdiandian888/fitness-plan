import os
import sys

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f'Script directory: {script_dir}')
print(f'Current working directory: {os.getcwd()}')

# 在脚本目录创建文件
output_path = os.path.join(script_dir, 'final_test.txt')
with open(output_path, 'w') as f:
    f.write('Success!')
    
print(f'Created file at: {output_path}')
print(f'File exists: {os.path.exists(output_path)}')
