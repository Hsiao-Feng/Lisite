# -*- coding: utf-8 -*-
import markdown
def md2html(file):
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()
        html = markdown.markdown(text, extensions=['fenced_code'])
    return html