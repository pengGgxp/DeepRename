# DeppRename

该项目基于LLM(DeepSeek)实现读取文件内容并对文件进行重命名的功能。

# 当前支持文件类型

- txt
- pdf
- docx
- pptx
- xlsx,xls

## 运行环境

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![UV 0.6.17+](https://img.shields.io/badge/uv-0.6.17+-red)]()

## 运行方法

### 1. 安装依赖

``` bash
uv pip install -e .
```
### 2. 方式一：运行程序,默认读取当前目录下的所有文件，并重命名所有文件
``` python
uv run main.py
```
### 3. 方式二：指定文件夹路径，并重命名所有文件

```
uv run main.py -d /path/to/folder
```

## 打包方法

``` bash
uv run pyinstaller -D -F main.py
```

## 功能

- 命令行输入文件夹路径
- 直接运行 会自动重命名当前目录下的所有文件

