# mdtTextConverter

[Korean](./README.md) | [English](./README-en_EN.md)

mdt에 있는 몬스터, npc 이름을 [wowhead](https://www.wowhead.com)의 db를 참조하여 한글로 변경하는 프로그램.

## 필요 프로그램

- Python

- Selenium

- Chrome Driver

## 설치 및 실행

1. main.py를 다운받는다.

2. 터미널에서 selenium을 설치한다.

   - pip install selenium

3. 크롬드라이버를 C:\ChromeDriver에 chromedriver라는 이름으로 둔다.

4. main.py를 실행한다.

## 규약

입력 순서는 아래와 같다.

    1. 변환할 데이터의 개수를 입력한다.

    2. 1번에 입력한 라인만큼 변환할 데이터를 입력한다.

입력 데이터 양식은 아래와 같다.

변환할 데이터가 Nokhud Saboteur일 때..

L["Nokhud Saboteur"] = "Nokhud Saboteur"

출력 데이터 양식은 아래와 같다.

L["Nokhud Saboteur"] = "노쿠드 파괴공작원"

## 개선 사항 (To-Do)

- NoN

## 개발 기록

- 2023.02.16 한 줄 변환 성공

- 2023.02.19 언어 선택자 수정

- 2023.02.25 npc 탭으로 이동하여 변환하는 기능 추가
