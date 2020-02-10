import requests, re, datetime
from bs4 import BeautifulSoup
import json

class MovieCrawling():
    def __init__(self):
        self.movieHrefs = []
        self.movieData = []

    def get_date(self):
        now = datetime.datetime.now()
        if now.month < 10:
            month = '0' + str(now.month)
        else:
            month = str(now.month)

        if now.day < 10:
            day = '0' + str(now.day)
        else:
            day = str(now.day)

        today = str(now.year) + month + day
        return today

    def save_Image(self, genre):
        res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=' + self.get_date() + '&tg=' + genre )
        soup = BeautifulSoup(res.text, 'html.parser')

        divs1 = soup.findAll('div', {'class': 'tit5'}, limit= 10)

        for div in divs1:
            links = div.find('a')
            movieHref = links['href']
            self.movieHrefs.append(movieHref)

        for movie in self.movieHrefs:
            res = requests.get('http://movie.naver.com' + movie)
            soup = BeautifulSoup(res.text, 'html.parser')

            posters = soup.findAll('div', {'class': 'mv_info_area'})

            mv_info = []
            for poster in posters:
                mv = poster.find('div', {'class': 'poster'})
                link = mv.find('a')
                img = link.find('img')
                title = img['alt']
                img_src = img['src']
                title = re.sub('[^0-9a-zA-zㄱ-힗]', '', str(title))
                
                #mv_info.append(title)
                #mv_info.append(img_src)
                self.movieData.append(title)
                self.movieData.append(img_src)
        
        #dict(zip(range(len(self.movieData)), self.movieData)
        
        return self.movieData
