"""
고려대학교 수강신청 크롤링 코드
Author: 장유영
Made on August 06, 2018
You can use this code freely,
but since this code includes Intellectual Property, please do not distribute this code with no permission.
"""


# Setting
# import traceback
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import pandas as pd
from pandas import Series, DataFrame


# Input 설정
path = str(Input())
'C:/Users/YY/Documents/'



# pd.set_option('display.max_columns', 50)

# 몇 가지 변수 선언
dict = {'간호대학':{'sign':'0231', '간호학과':'0233'},
        '경영대학':{'sign':'0140', '경영학과':'0142'},
        '공과대학':{'sign':'0217', '기계공학부':'4952', '산업경영공학부':'5320', '신소재공학부':'4630', '전기전자공학부':'5597',
                '건축사회환경공학부':'5204', '건축학과':'4887', '화공생명공학과':'4084'},
        '국제학부':{'sign':'3928', '국제학부':'3931'},
        '디자인조형학부':{'sign':'5338', '디자인조형학부':'5339'},
        '문과대학':{'sign':'0143', 'EML융합전공':'5672', '과학기술학융합전공':'4601', '국어국문학과':'0145',
                '노어노문학과':'0156', '독어독문학과':'0153', '불어불문학과':'0154', '사학과':'0803',
                '사회학과':'0152', '서어서문학과':'0158', '심리학과':'0151', '언어학과':'4391',
                '영어영문학과':'0146', '일어일문학과':'0157', '중어중문학과':'0155', '철학과':'0147', '한문학과':'0159'},
        '미디어학부':{'sign':'5256', '미디어학부':'5257'},
        '보건과학대학':{'sign':'4669', '바이오시스템의과학부':'5694', '바이오의공학부':'5693',
                   '보건정책관리학부':'5696', '보건환경융합과학부':'5695', '식품영양학과':'4676'},
        '사범대학':{'sign':'0234', '가정교육과':'0238', '교육학과':'0236', '국어교육과':'0240', '수학교육과':'0239',
                '역사교육과':'0241', '영어교육과':'0241', '지리교육과':'0242'},
        '생명과학대학':{'sign':'4652', '생명공학부':'4654', '생명과학부':'4653', '환경생태공학부':'4656',
                  '식품공학과':'5564', '식품자원경제학과':'4657'},
        '정경대학':{'sign':'0197', '경제학과':'0200', '정치외교학과':'0199', '통계학과':'0201', '행정학과':'0203'}}

# 단과대학 이름을 담은 리스트
college_list = list(dict.keys())

# 데이터를 저장할 빈 데이터프레임
df = DataFrame(columns=['College', 'Major', 'Contents'])


# 크롬 드라이버로 크롤링 후 df라는 데이터프레임에 자료 저장
def driver_control():
    global df
    driver = webdriver.Chrome('C:/Users/YY/Documents/Winter Project/chromedriver')
    driver.get('http://sugang.korea.ac.kr/')
    driver.implicitly_wait(3)

    # frame이 명시적으로 드러나있지 않으므로 활동범위를 firstF frame으로 옮겨준다.
    driver.switch_to.frame(driver.find_element_by_name('firstF'))
    # print(driver.page_source)

    # 로그인 과정
    driver.find_element_by_name('id').send_keys('2013150005')
    driver.find_element_by_name('pw').send_keys('pianist522')
    driver.find_element_by_xpath("//*[@id='loginButton']/ul/li/a/img").click()

    # 팝업창을 날려준다.
    while True:
        time.sleep(0.3)
        try:
            a = driver.switch_to.alert
            a.accept()
            break
        except NoAlertPresentException as e:
            print(e)
            # traceback.print_exc()

    # 다시 홈 화면으로 돌아간다.
    driver.get('http://sugang.korea.ac.kr/')

    # 탭에서 과목조회-학부전공과목을 클릭한다.
    driver.switch_to.frame(driver.find_element_by_name('secondF'))
    driver.find_element_by_id('main1').click()
    driver.find_element_by_xpath("//*[@id='sub1']/li[1]/a").click()

    # secondF frame에서 빠져나와 원래 활동범위로 복귀한다.
    driver.switch_to_default_content()

    # 다시 firstF frame으로 들어간다.
    driver.switch_to.frame(driver.find_element_by_name('firstF'))
    driver.switch_to.frame(driver.find_element_by_name('ILec'))

    # 반복 파싱 시작

    for i in range(0, len(college_list)):
        # 그 단과대학의 Option Value: 예) 간호대학 = '0231'
        college_name = list(dict.keys())[i]
        college_sign = list(dict.values())[i]['sign']

        # Webdriver는 Select 옵션에서 해당 단과대학을 선택한다.
        driver.find_element_by_xpath("//option[@value='" + str(college_sign) + "']").click()

        # 단과대학을 선택하고 나서는 이제 소속 전공을 선택해야 한다.
        # list(dict.values())[i]는 i번째 단과대학의 내부 딕셔너리를 가리킨다.
        # 이것의 length를 구하면 소속 전공의 수 + 1이 된다. (sign이라는 멤버가 추가적으로 들어가 있기 때문)
        # 그대로 range(0, ~)을 하면 문제 없이 소속 전공의 수에 맞게 구할 수 있다.
        for j in range(0, len(list(dict.values())[i])):
            # j = 0이면 sign 멤버를 찾게 되기 때문에 무시한다.
            if j == 0:
                pass
            # 본격적으로 j = 1부터 내부 파싱을 시작한다.
            else:
                # 소속 전공을 클릭한 후 조회버튼을 클릭한다.
                major_sign = list(list(dict.values())[i].values())[j]
                driver.find_element_by_xpath("//option[@value='" + str(major_sign) + "']").click()
                driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/div[1]/span[2]/input").click()

                # tag name을 통해 html 구조 안으로 진입한다.
                driver.find_element_by_tag_name("table")
                driver.find_element_by_tag_name("tbody")

                # contents는 tr 태그 내부에 있는 모든 element를 모은 리스트이다.
                contents = driver.find_elements_by_tag_name("tr")

                # 텍스트를 모을 빈 리스트를 생성한다.
                texts = []

                # contents 리스트 내에 있는 원소들을 하나씩 꺼내서 사용할 것이다.
                # content는 contents의 k번째 element이다.
                # 그 content에 있는 text를 texts 리스트에 담는다.
                for k in range(1, len(contents)):
                    content = contents[k]
                    t = content.text
                    texts.append(t)

                # texts에는 타겟 전공의 과목 정보가 모드 담겨 있다.
                # 만약 간호학과의 전공이 총 60개 개설되었다면 texts 리스트에는 총 60개의 element가 담겨 있다.
                ser3 = Series(texts)

                # 이후에 데이터프레임을 만들기 위해
                # 위 element개수에 맞는 길이를 가진 Series를 생성하는데,
                # 하나는 전공 이름을 담고, 하나는 단과대학 이름을 담는다.
                # 이렇게 단과대학 내부의 1개의 전공에 대해 총 3개의 Series를 만든다.
                major_name = list(list(dict.values())[i].keys())[j]
                ser2 = Series([major_name] * len(contents))
                ser1 = Series([college_name] * len(contents))

                unit_major = DataFrame({'College': ser1, 'Major': ser2, 'Contents': ser3})

                df = pd.concat([df, unit_major], axis=0)
    return df


def edit_df(df):
    # NA열을 날려주고(정보 없음)
    df = df.dropna(inplace=False)

    # Index도 초기화 해준다.
    df = df.reset_index()
    # df.isnull().sum()

    # 정리된 데이터를 담을 새 데이터프레임을 선언한다.
    Course = DataFrame(columns=['College', 'Major', 'code', 'rest'])
    Course['College'] = df['College']
    Course['Major'] = df['Major']

    for i in range(0, len(df['Contents'])):
        element = df['Contents'][i]
        element = element.replace('\n', ' ')
        splited = element.split(' ')

        code = splited[1]
        rest = ' '.join(splited[5:])

        Course['code'][i] = code
        Course['rest'][i] = rest

    Course.to_csv(os.path.join(path, 'EGI_sugang_2018.csv'), index=False, encoding='CP949')


def main():
    df = driver_control()
    edit_df(df=df)


if __name__ == '__main__':
    main()
