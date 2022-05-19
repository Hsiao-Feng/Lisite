# Lisite
**Lisite** is a lightweight site generation program. It uses Markdown to generate HTML site. Lisite is "lite" and "site".

**Lisite** 是一款轻量级站点生成程序，可从 Markdown 文件生成页面。使用 Python 3 环境，借以 Jinja2 实现。Lisite 是指“lite”和“site”。

## 安装
安装依赖——`jinja2`和`markdown`。

    pip install jinja2
    pip install markdown

## 使用

将配置信息填入`config.py`，运行`make.py`。程序将搜寻`raw`目录下的 Markdown 文件，站点将在`public`目录下生成。

```python
#是否启用 HTTPS
enable_https = False

#域名，可带端口
domain = "localhost"

#路径，路径结尾不应有“/”。如果是根目录，则留作空字符串
path = "" # e.g.:  "/blog"

#站点名
name = "LISITE DEMO"

#站点简介
bio = "A simple demo for lisite."

#采用主题的文件夹名，可在 /theme 目录下找到
theme = "Pinghsu_Lite"
```

关于 Markdown 文件在 Lisite 生成时的特殊规范，请阅读 [`raw/demo.md`](./raw/demo.md) 了解如何使用。

## 默认主题

默认主题 PingHsu Lite 修改自 [Chakhsu](https://github.com/chakhsu/) 为 [Typecho](http://typecho.org) 博客程序开发的 [Pinghsu](https://github.com/chakhsu/pinghsu) 主题。原主题的许可为 [MIT License](https://github.com/chakhsu/pinghsu/blob/master/LICENSE.md)，本主题同样遵循本许可。

在此感谢 Chakhsu 做出的贡献。