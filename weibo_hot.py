# 程序功能：爬取微博热搜榜数据
# 原创作者：马哥python说
# 联系方式：公众号"老男孩的平凡之路"

import pandas as pd  # 存入excel数据
import requests  # 向页面发送请求
from bs4 import BeautifulSoup as BS  # 解析页面


def get_weibo_hot():
	"""爬取微博热搜排行榜数据"""
	# 目标地址
	url = 'https://s.weibo.com/top/summary?cate=realtimehot'
	# 请求头
	header = {
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"accept-encoding": "gzip, deflate",
		"accept-language": "zh-CN,zh;q=0.9",
		"cache-control": "max-age=0",
		"cookie": "换成自己的cookie",
		"priority": "u=0, i",
		"sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		"sec-ch-ua-mobile": "?0",
		"sec-ch-ua-platform": "macOS",
		"sec-fetch-dest": "document",
		"sec-fetch-mode": "navigate",
		"sec-fetch-site": "none",
		"sec-fetch-user": "?1",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
	}
	# 发送请求
	r = requests.get(url, headers=header) 
	# 解析页面
	soup = BS(r.text, 'html.parser')
	items = soup.find_all('tr')[1:]
	text_list = []  # 标题
	href_list = []  # 链接地址
	order_list = []  # 排名
	type_list = []  # 热搜类别
	view_count_list = []  # 热度
	for i in items:
		# 链接地址
		href = i.find('td', {'class': 'td-02'}).find('a').get('href')
		href_list.append('https://s.weibo.com' + href)
		# 排名
		try:
			order = i.find('td', {'class': 'td-01'}).text
		except:
			order = ""
		order_list.append(order)
		# 热度
		try:
			view_count = i.find('td', {'class': 'td-02'}).find('span').text.split(' ')[-1]
		except:
			view_count = ""
		view_count_list.append(view_count)
		# 热搜类别
		try:
			icon_type = i.find('td', {'class': 'td-03'}).find('i').text
		except:
			icon_type = ""
		type_list.append(icon_type)
		# 标题
		text = i.find('td', {'class': 'td-02'}).find('a').text.strip()
		print(order, text)
		text_list.append(text)
	df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
		{
			'热搜标题': text_list,
			'热搜排名': order_list,
			'热搜类别': type_list,
			'热度': view_count_list,
			'链接地址': href_list
		}
	)
	df.to_excel('微博热搜榜.xlsx', index=False)  # 保存结果数据


if __name__ == '__main__':
	get_weibo_hot()
	print('\n爬虫运行完毕，请检查：微博热搜榜.xlsx')
