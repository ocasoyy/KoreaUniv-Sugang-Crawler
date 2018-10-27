작성자: 28기 장유영
<조건>
1) 파이썬3이 설치되어 있어야 합니다.
2) Windows OS만 사용가능합니다. 그 외에는 코드를 직접 수정하세요.
3) 반드시 제일 아래에 있는 주의사항을 읽어보세요.

<준비 작업>
1) chromedriver.zip파일의 압축을 풀고 chromedriver.exe파일을 본인이 원하는 위치에 갖다 놓습니다.
 * 이 때 한글 경로가 포함된 폴더에 저장하지 마십시오.
2) EGI_Crawler.py역시 같은 위치에 갖다 놓습니다. (사실 꼭 같을 이유는 없습니다. 원하는 위치에 갖다 놓아도 됩니다.)
3) 위 2개 파일의 경로를 복사해 놓습니다.

<메인 커맨드>
1) 파이썬 3.6을 설치하고 명령프롬프트를 켠다. 이후 아래 입력: 
2) 입력: cd EGI_Crawler.py를 저장한 위치
 * 제 컴퓨터에서는 cd C:/Users/YY/Documents/Deep_Learning/Crawling 라고 입력했겠죠?
3) 입력: python EGI_Crawler.py
4) 입력: 문서를 저장할 경로
 * 제 컴퓨터에서는 C:/Users/YY/Documents
5) 입력: 크롬 드라이버 저장 위치
 * 제 컴퓨터에서는 C:/Users/YY/Documents/Winter Project/chromedriver
6) 입력: 본인의 ID & PW

<참고>
EGI_Crawler.py를 저장한 위치
C:/Users/YY/Documents/Deep_Learning/Crawling

문서를 저장할 경로
C:/Users/YY/Documents

크롬드라이버 저장 위치
C:/Users/YY/Documents/Winter Project/chromedriver

<주의사항>
명령프롬프트에 경로를 입력할 때 4, 5번의 경우 절대 \(역슬래시)를 입력하면 안됩니다. 반드시 /로 고쳐주세요.