# -*- coding: utf-8 -*-
import time
import config
import os
import markdown2html as mp
from jinja2 import Environment, FileSystemLoader

startTime = time.time()

prefix = config.enable_https and "https://" or "http://"

env = Environment(loader=FileSystemLoader('./'))
template = env.get_template(f'./theme/{config.theme}/content.html.j2')
titleList = []
# 遍历 ./raw 下的 md 文件
for i in os.walk('./raw'):
    for j in i[2]:
        if j.endswith('.md'):
            # 获取文件名
            title = j.split('.')[0]
            #获取第 2-4 行
            with open('./raw/' + j, 'r', encoding='utf-8') as f:
                text = f.readlines()[1:4]
                text = [i.strip() for i in text]
                item = {
                    'title': text[0],
                    'date': text[1],
                    'description': text[2],
                    'link': title
                }
                titleList.append(item)
            with open(f"public/{title}.html",'w',encoding='utf-8') as fout:   
                content = template.render(
                    name = config.name, 
                    title = text[0],
                    date = text[1],
                    bio = config.bio,
                    url = prefix + config.domain + config.path,
                    content = mp.md2html(f'./raw/{title}.md')
                )
                fout.write(content)
titleList.sort(key=lambda x: x['date'], reverse=True)
template = env.get_template(f'./theme/{config.theme}/index.html.j2')
with open(f"public/index.html",'wb') as fout:   
    content = template.render(
        name = config.name, 
        titleList = titleList,
        bio = config.bio,
        url = config.domain + config.path
    ).encode('utf-8')
    fout.write(content)

# 复制 style.css 文件
with open(f'./public/style.css','wb') as fout:
    with open(f'./theme/{config.theme}/style.css','rb') as fin:
        fout.write(fin.read())

useTime = time.time() - startTime
print("Done.");
print("Use time: %.2f s." % useTime)
print(f"Total: {len(titleList)} posts.")
print("Have a good day ;)")