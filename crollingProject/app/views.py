from django.shortcuts import render, redirect
from .models import mlonList
from bs4 import BeautifulSoup
import requests

# Create your views here.
def index(request):
    list = mlonList.objects.all()
    return render(request, 'index.html', {'list':list})

iamhuman = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
url = "https://www.melon.com/chart/day/index.htm"

def melonCrolling():
    req = requests.get(url, headers=iamhuman) # 자동화 금지 페이지에 요청을 할 때 나의 정보를 보여줌
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    # find_all 외에도 많은 문법이 있지만 필요할때마다 크롤링해서 찾아쓰기 li에 있는 nav_item을 모두 가져온다!
    # 필요한 거를 사이트내에서 검사해서 가져오기

    # select와 find는 무엇이 다를까요?
    # select는 css selector를 허용하는 반면, find는 그럴 수 없다
    song = soup.find_all('div', {"class":"ellipsis rank01"})
    album = soup.find_all('div', {"class":"ellipsis rank03"})
    singer = soup.find_all('div', {"class":"ellipsis rank02"})
    rank = soup.find_all('span', {"class":"rank"})
    #우클릭 -> 검사 -> Copy selector
    albumImg = soup.select('td:nth-child(4) > div > a > img') #50위까지밖에 안나오네? 51위를 검사해보자! 아 다르다!!! 그럼 #lst50을 지우장 ^^ (or #lst100도 똑같이 씀. 하지만 중복 코드는 지양한다!)


    # 나중에 가공하기 위해 append 를 사용하여 빈 리스트에 저장
    songs = []
    albums = []
    singers = []
    ranks = []
    imgs = []

    for i in song:
        songs.append(i.find('a').text) #value를 써야함
    for j in album:
        albums.append(j.find('a').text)
    for k in singer:
        singers.append(k.find('a').text)
    for l in rank[1:]:
        ranks.append(l.text)
    for z in albumImg:
        imgs.append(z.get("src")) #모든 곳에서 이렇게 사용되진 않음. 잘 찾아서 사용!

    # print(len(song))
    # print(songs)
    # print(albums)
    # print(singers)
    # print(ranks)
    # print(imgs[0])
    # print(len(imgs))

    sumlist = list(zip(songs,singers,ranks,imgs)) #나중에 html에 보내주기 위함
    return(sumlist)

def crolling(request):
    Melon_data_list = melonCrolling()
    mlonList.objects.all().delete()
    for i in range(len(Melon_data_list)):
        mlonList(
            songName=Melon_data_list[i][0],
            singerName=Melon_data_list[i][1],
            rankNumber = Melon_data_list[i][2],
            imgScr = Melon_data_list[i][3]
        ).save()
    return redirect('index')