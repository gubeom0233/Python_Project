from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

# 파일 생성일
time = datetime.datetime.today()
TIME = time.strftime('%Y-%m-%d')

# 출력 파일 명
OUTPUT_FILE_NAME = 'clien_programming_list_crawler_' + TIME + '.txt'
URL = "https://www.clien.net/service/board/cm_app"
BASE_URL = "https://www.clien.net/"

# 클리앙 개발한당 첫번째 페이지 게시글 크롤링
def get_text(URL, BASE_URL):
    html = urlopen(URL)
    soup = BeautifulSoup(html, "html.parser")
    base_url = BASE_URL
    clien_programming_urls = []
    clien_programming_titles = []    

    list_a = soup.find_all('a', {'class':'list_subject'})
    list_titles = soup.find_all('span', {'class':'subject_fixed'})

    text = ''
    for list_link in list_a:
        link = base_url + list_link.attrs['href']
        clien_programming_urls.append(link)

    for list_title in list_titles:
        title = list_title.attrs['title']
        clien_programming_titles.append(title)
        
    for index, clien_programming_url in enumerate(clien_programming_urls):
        html = urlopen(clien_programming_url)
        soup = BeautifulSoup(html, "html.parser")
        title = clien_programming_titles[index]
        url = clien_programming_url
        text = text + str(index+1) + ' ' + title + ' ' + url + '\n'

    return text

# 메인 함수 실행
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL, BASE_URL)
    open_output_file.write(result_text)
    open_output_file.close()
    
 
if __name__ == '__main__':
    main()