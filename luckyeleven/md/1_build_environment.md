# Build Environment

## Scrapy搭建
- 参考：[install guild](https://docs.scrapy.org/en/latest/intro/install.html#)
- 环境: python 2.7
- 安装scrapy依赖
```text
pip install scrapy
```
- 新建project
```text
scrapy startproject tutorial
```
- 目录结构介绍
```text
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```
- 