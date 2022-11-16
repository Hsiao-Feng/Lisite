# Lisite

[English README](#lisite---english)

**Lisite** is a lightweight site generation program. It implemented in Jinja2 using Python 3 environment. It uses Markdown to generate HTML site. Lisite is "lite" and "site".

**Lisite** 是一款轻量级站点生成程序，可从 Markdown 文件生成页面。使用 Python 3 环境，借以 Jinja2 实现。Lisite 是指“lite”和“site”。

## 安装
安装依赖——`jinja2`和`markdown`。

    pip install jinja2
    pip install markdown

## 使用

将配置信息填入`config.py`，运行`make.py`。程序将搜寻`raw`目录下的 Markdown 文件，站点将在`public`目录下生成。

```python
# 是否启用 HTTPS
enable_https = False

# 域名，可带端口
domain = "localhost"

# 路径，路径结尾不应有“/”。如果是根目录，则留作空字符串
path = "" # e.g.:  "/blog"

# 站点名
name = "LISITE DEMO"

# 站点简介
bio = "A simple demo for lisite."

# 采用主题的文件夹名，可在 /theme 目录下找到
theme = "Pinghsu_Lite"
```

要使用 Lisite，您需要使 Markdown 的前 5 行是用于 Lisite 解读的信息，遵循以下格式：

```html
<!--
标题
YYYY/MM/DD hh:mm
描述
-->
```

例如：

```html
<!--
欢迎使用 Lisite
2022/05/19 12:00
一篇使用教程
-->
```

此外，您需要使文档以`.md`结尾，以便程序识别。

运行 `make.py` 即可生成 HTML 文件至 `public` 文件夹下。

```shell
python3 make.py
```

## 默认主题

默认主题 PingHsu Lite 修改自 [Chakhsu](https://github.com/chakhsu/) 为 [Typecho](http://typecho.org) 博客程序开发的 [Pinghsu](https://github.com/chakhsu/pinghsu) 主题。原主题的许可为 [MIT License](https://github.com/chakhsu/pinghsu/blob/master/LICENSE.md)，本主题同样遵循本许可。

在此感谢 Chakhsu 做出的贡献。

# Lisite - English

**Lisite** is a lightweight site generation program. It implemented in Jinja2 using Python 3 environment. It uses Markdown to generate HTML site. Lisite is "lite" and "site".

## Installation

Install dependencies - `jinja2` and `markdown`.

    pip install jinja2
    pip install markdown


## Use

Fill in the configuration information into `config.py` and run `make.py`. The program will search for Markdown files in the `raw` directory, and the site will be generated in the `public` directory.

```python
# Whether to enable HTTPS
enable_https = False

# Domain name, with port available if required
domain = "localhost"

# Path, there should be no "/" at the end of the path. 
# If it is the root directory, leave it as an empty string
path = "" # e.g.:  "/blog"

# Site name
name = "LISITE DEMO"

# Site bio
bio = "A simple demo for lisite."

# The theme's folder name, which can be found in the /theme directory
theme = "Pinghsu_Lite"
```

To use Lisite, you need to make the first 5 lines of Markdown the information for Lisite interpretation, following the format:
```html
<!--
Title
YYYY/MM/DD hh:mm
Description
-->
```

For example:

```html
<!--
Welcome to Use Lisite
2022/05/19 12:00
A tutorial
-->
```
You need to make the document end with `.md` for the program to recognize it.

Run `make.py` to create HTML files in `public` folder.

```shell
python3 make.py
```


## Default Theme

The default theme PingHsu Lite is modified from [Pinghsu Theme](https://github.com/chakhsu/pinghsu) developed by [Chakhsu](https://github.com/chakhsu/) for [Typecho](http://typecho.org) blog program. The license of the original theme is [MIT License](https://github.com/chakhsu/pinghsu/blob/master/LICENSE.md), and this theme also follows this license.

Thanks to Chakhsu for his contribution.