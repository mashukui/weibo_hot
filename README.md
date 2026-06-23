# 微博热搜榜爬虫/Weibo Hot Search Crawler

> 基于Python3的微博热搜榜数据采集脚本，支持热搜标题、排名、热搜类别、热度值和详情链接等核心字段导出。

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+"></a>
  <a href="https://pypi.org/project/requests/"><img src="https://img.shields.io/badge/requests-required-green.svg" alt="requests"></a>
  <a href="https://pypi.org/project/pandas/"><img src="https://img.shields.io/badge/pandas-required-orange.svg" alt="pandas"></a>
</p>

## 📖 项目简介

本项目是一个面向Python爬虫初学者的微博热搜采集示例。脚本通过请求微博热搜榜页面，解析页面中的热搜表格数据，并将热搜内容整理为Excel文件，方便后续用Excel、Python或其他数据分析工具处理。

源码结构简单，适合学习以下内容：

- 使用`requests`发送HTTP请求
- 解析HTML页面结构
- 提取列表数据中的核心字段
- 使用`pandas`生成表格数据
- 将结果保存为Excel文件

## ✨ 功能特点

- 自动抓取微博热搜榜数据
- 自动生成热搜排名
- 支持提取标题、热度值、热搜类别和链接
- 保存为`xlsx`文件，方便直接用Excel打开
- 代码结构简单，适合入门学习

## 📊 采集字段

| 字段 | 说明 | 示例 |
| --- | --- | --- |
| 热搜排名 | 当前热搜排序 | 1 |
| 热搜标题 | 热搜事件或话题标题 | 高考成绩 |
| 热搜类别 | 平台返回的热搜标记 | 热 / 新 / 荐 |
| 热度 | 当前热搜热度值 | 1868943 |
| 链接地址 | 热搜详情页链接 | [https://s.weibo.com/weibo?q=...](https://s.weibo.com/weibo?q=%E9%AB%98%E8%80%83%E6%88%90%E7%BB%A9&t=31&band_rank=1&Refer=top) |

## 📄 运行结果示例

脚本运行完成后，会在当前目录生成：

```text
微博热搜榜.xlsx
```

Excel示例：

| 热搜标题 | 热搜排名 | 热搜类别 | 热度 | 链接地址 |
| --- | --- | --- | --- | --- |
| 高考成绩 | 1 | 热 | 1868943 | [https://s.weibo.com/weibo?q=...](https://s.weibo.com/weibo?q=%E9%AB%98%E8%80%83%E6%88%90%E7%BB%A9&t=31&band_rank=1&Refer=top) |
| 哈兰德偷喝对方门将的水 | 2 |  | 968233 | [https://s.weibo.com/weibo?q=...](https://s.weibo.com/weibo?q=%23%E5%93%88%E5%85%B0%E5%BE%B7%E5%81%B7%E5%96%9D%E5%AF%B9%E6%96%B9%E9%97%A8%E5%B0%86%E7%9A%84%E6%B0%B4%23&t=31&band_rank=2&Refer=top) |
| 万千气象看重庆 | 3 | 新 | 967606 | [https://s.weibo.com/weibo?q=...](https://s.weibo.com/weibo?q=%23%E4%B8%87%E5%8D%83%E6%B0%94%E8%B1%A1%E7%9C%8B%E9%87%8D%E5%BA%86%23&t=31&band_rank=3&Refer=top) |

## 🚀 快速开始

### 环境要求

- Python3.8+
- Windows/macOS/Linux

### 安装依赖

```bash
pip install requests pandas beautifulsoup4 openpyxl
```

### 基本使用

```bash
python3 weibo_hot.py
```

运行时终端会输出热搜排名和标题。运行完成后，采集结果会保存到`微博热搜榜.xlsx`。

## ⚙️ 核心原理

### 请求地址

```text
https://s.weibo.com/top/summary?cate=realtimehot
```

### 请求头

脚本需要配置可用的`Cookie`，否则页面可能无法正常返回热搜数据。

```python
header = {
    "user-agent": "Mozilla/5.0 ...",
    "cookie": "换成自己的cookie"
}
```

### 核心流程

1. 请求微博热搜榜页面
2. 使用`BeautifulSoup`解析HTML
3. 遍历热搜表格中的每一行
4. 提取`热搜标题`、`热搜排名`、`热搜类别`、`热度`、`链接地址`
5. 使用`pandas.DataFrame`整理数据
6. 导出为Excel文件

## 🎯 适用场景

- Python爬虫入门练习
- 热点事件观察
- 热搜数据归档
- Excel数据处理学习
- pandas表格生成示例

## ❓ 常见问题

### 运行后没有生成Excel怎么办？

先确认依赖是否安装成功：

```bash
pip install requests pandas beautifulsoup4 openpyxl
```

再确认当前目录是否有`weibo_hot.py`，并在脚本所在目录运行命令。

### 为什么脚本会返回空数据？

微博页面结构和反爬策略可能发生变化。先检查`Cookie`是否有效，再确认页面的`tr`、`td-02`、`td-03`等结构是否变化。

### 是否需要Cookie？

当前脚本需要Cookie。请不要把个人Cookie、账号密码等敏感信息提交到公开仓库。

## ⚠️ 注意事项

- 请合理控制运行频率，避免对目标站点造成压力。
- 本项目仅用于学习研究，不建议用于商业采集或批量抓取。
- 页面结构和字段内容可能随目标网站调整而变化。
- 使用本项目时，请自行遵守目标网站的服务条款、robots规则以及相关法律法规。

## 📌 免责声明

本项目仅供学习和研究使用。因使用本项目产生的任何问题或后果，由使用者自行承担。
