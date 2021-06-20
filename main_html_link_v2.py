# -*- coding: utf-8 -*-
#このコードはjinja2_main_html_link_va.tmplファイルをインポートする。
from selenium import webdriver
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import datetime
from webdriver_manager.chrome import ChromeDriverManager


env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
urls = [
'UCV_e5CE026DKpkXEeXvo3cQ',	#トラック野郎USA 20201128-20210124はまだ　0125-0320の期間はlist
'UC9D8vopYTSvGIdzyH6e_3oA',	#YMK_iPadで生活を少し豊かに 20210321DL済
'UCcXtyjK8wagT5LWS5bBgPPQ',	#amity_sensei 20210321DL済
'UC1kS0UwEOoHpgzgnV_goVZQ',	#清水貴裕　20210321DL済
'UCvoAeGZoC8giXP59NOZABIA',	#NEMOPHILA 20210321DL済
# 'UCCRkkf0qy8nYkROdJU7u20w',	#にゃんえり 20210321DL済
# 'UCHFfKPuB2rra43wU8HcemPg',	#ガチャとＴＶ 20210321DL済
# "UC7J7894vBpQsTQTt-NlBhoA",	#地球遊戯 20210321分までダウン済み
# 'UC-IdN5EFZvzzZGqgul8eXKQ', #戸田覚　l20210321_DL済み
# 'UC3A0nuJpz3NnPi2luPj41fA',	#KenrickSound
# 'UC1rDo_9Mb4bcynWoqeGbLig', 	#もか太郎 20210321DL済
# 'UCDLQNVQRPRK0_lJFtgqKNUw', #Taka Shigeta 20210321DL済
# 'UC7I3QTra4_kC4TSu8f7rHkA', 	#マコなり社長 
# 'UCuhg79_V-Q9hd2feSzCYSUw', 	#Jacob Koller Japan_PianoJazz
# 'UCuFW_SrYtpktBaShHay174A', 	#GIRLFRIEND 20210321DL済
# 'UCLPHXwLp90A5R69Eltxo-sg',  #ムーザルチャンネル 20210321DL済
# 'UCo12b5NHD4v9wSZ_ditKSlA', 	#D-Studio 20210321DL済
'UCxZ0BkYadR-0LtmkrHcFOvQ', #せろりんね 20210321DL済
# 'UC4rlAVgAK0SGk-yTfe48Qpw', 	#BRIGHT SIDE
# 'UCTfta7Ult6yLu7ru-WInOGg', 	#drikin
 'UCj0Adro_5w2joqip5JuR0_Q', 	#あおたび
# 'UCeJYDunL9xZtmczAP9AGmFA', #アスキー
# 'UCY3J0X26AAeqIijVE1kANIw', 	#DaVinci Resolve & ATEM チュートリアルビデオ集
# 'UCg5SnU8xJ7jYNrzNffsD-5A',  #omokage Davinch Resolve
# 'UCKF5a-oFD9fuwheuos30y2w',  #ASRockJapan
# 'UCom2Kwi5JiX5NFSF-jXnzZg',  	#はなきんTV
#'',  #
#'',  #
#'',  #
#'',  #
]

tmpl = env.get_template('jinja2_main_html_link_v2.tmpl')
items=[]
def main():
	#driver = webdriver.Chrome()
	driver = webdriver.Chrome(ChromeDriverManager().install())
	for url in urls:
		#driver.get('https://www.youtube.com/channel/{}/videos?view=0&flow=grid'.format(url))
		driver.get('https://www.youtube.com/channel/{}/videos?view=0&sort=dd&flow=grid'.format(url))
		content = driver.page_source.encode('utf-8').strip()
		soup = BeautifulSoup(content, 'html.parser')
		#print(soup)
		titles = soup.findAll('a', id ='video-title')
		views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')#視聴回数と経過日数<span class="style-scope ytd-grid-video-renderer">6 日前</span>
		video_urls = soup.findAll('a', id='video-title')
		#Channel_name 自作部分
		Channel_name = soup.find('link',itemprop="name")
		print(Channel_name.get("content"))
		
		print('Channel: https://www.youtube.com/{}'.format(url))
		i=0
		j=0

	#print(titles)
		
		for title in titles[:1]:
			#f=open('youtube_20210328.txt','a', encoding='UTF-8')
			#f.write(str('\n{}\t{}\t{}\thttps://www.youtube.com/{}'.format(title.text, views[i].text, views[i+1].text, video_urls[j].get('href'))))
			#f.close()
			items.append({"title":title.text, "views":views[i].text, "befora":views[i+1].text, "url":'https://www.youtube.com' + video_urls[j].get('href')})
			#print(items)
			#print('\n{}\t{}\t{}\thttps://www.youtube.com/{}'.format(title.text, views[i].text, views[i+1].tetx, video_urls[j].get('href')))
			
			i+=2
			j+=1
	#f.close()
	datenow = datetime.datetime.now()
	html = tmpl.render({"items":items,"datenow":datenow})

	with open('20210620_TEST.html',mode='a',encoding="utf-8") as f:
		f.write(str(html))
main()

