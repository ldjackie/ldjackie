import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
# 获取节点
def get_top(url):
    respose = requests.get(url, headers=headers)
    soup = BeautifulSoup(respose.text, 'lxml')
    nums = soup.select('em')  # 获取排名节点
    titles = soup.find_all('div', class_='hd') # 获取电影名称节点
    actors = soup.find_all('p', class_='')  # 获取电影导演和演员节点
    links = soup.select('ol li div a')  # 获取链接节点
    rating_nums = soup.find_all('span', class_='rating_num') # 获取评分节点
    evaluate_numbers = soup.find_all('div', class_='star') #获取评价人数节点
    evaluates = soup.find_all('span', class_='inq')  # 获取评价节点
    # 将信息放进字典中
    for num, title, link, actor, rating_num, evaluate_number, evaluate in zip(nums, titles, links, actors, rating_nums,evaluate_numbers, evaluates):
        data = {  # 数据清洗
            '电影排名:\t': num.get_text(),
            '电影名称:\t': title.get_text().split('\n')[2],
            '电影链接:\t': link.get('href'),
            '电影导演:\t': actor.get_text().strip(),
            '电影评分:\t': rating_num.get_text().strip(),
            '评价人数:\t': evaluate_number.get_text().split('\n')[4],
            '评价内容:\t': evaluate.get_text()
        }
        print(data)
        # 写入txt文件
        file = open('.\Top250.txt', 'a', encoding='utf-8')
        for k, v in data.items():
            s = str(v)
            file.write(k + ' ')
            file.write(s + ' ')
            file.write('\n')
        file.close
 # 遍历10个URL
for i in range(11):
    urls = {'https://movie.douban.com/top250?start={}&filter='.format(i * 25)}
    for url in urls:
        get_top(url)