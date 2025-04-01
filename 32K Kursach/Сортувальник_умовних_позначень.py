import os
import subprocess


умовні_позначення='''
Django - бекенд фреймворк для Python-у
Python - мова програмування високого рівня
MongoDB - сучасна документна база даних
MySQL - популярна реляційна SQL база даних
'''.strip()

lines=умовні_позначення.split('\n')
pairs=dict([l.split(' - ') for l in lines])
pairs=dict(sorted(pairs.items(),key=lambda i: i[0]))
res: list[str] = []
for index,key in enumerate(pairs):
    value: str = pairs[key]
    last_symbol: str = value[-1]
    if last_symbol==';' or last_symbol=='.':
        pairs[key] = value[:-1]
    
    if index!=len(pairs)-1:
        pairs[key] += ';'
    else:
        pairs[key] += '.'

    current_result = f'{key} – {pairs[key]}'
    res.append(current_result)
resulting_string = '\n'.join(res)
print(resulting_string)
file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'Умовні_позначення.txt')
with open(file_path,encoding='utf-8',mode='w') as f:
    f.write(resulting_string)