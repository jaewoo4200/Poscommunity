# Django - Poscommunity

django로 만든 커뮤니티 사이트

# 내부 모듈

실행해서 없는 모듈 직접 설치 바람

# 외부 모듈

django

그 외엔 실행해서 없는 모듈 직접 설치 바람

# 실행 방법

manage.py 가 위치한 경로에서 터미널로 python manage.py runserver

-> localhost나 127.0.0.1로 들어가짐

python manage.py runserver 0.0.0.0:포트번호

->해당 포트 번호로 열림과 동시에, LAN서버에 있는 다른 컴퓨터에서도 접속 가능

*포트 번호 사용시 방화벽에서 해당 포트를 열어주어야 함. 서버 본인만)

django-admin createsuperuser

-> 관리자 계정 생성. 열린 웹사이트 주소 끝에 /admin을 입력하면 관리자 페이지로 이동