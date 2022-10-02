# Store Service
사용자의 일기를 생성, 조회, 수정, 삭제할 수 있는 서비스의 백엔드 API를 개발하여 제공합니다. 외부 API를 사용하여 생성 시 도시(서울)의 현재 날씨를 함께 등록할 수 있습니다.

---
## 목차
1. [사용법](#사용법)
2. [사용 기술 스택](#사용-기술-스택)
3. [MVP Service](#MVP-Service)
4. [API 명세서](#API-명세서)
5. [기능 명세서 및 분석](#기능-명세서-및-분석)
6. [구현 코드](#구현-코드)

<br>

---

## 사용법
- [가상 환경 설치](#가상-환경-설치)부터는 프로젝트 최상위 디렉토리(diary)에서 명령어를 입력하셔야 합니다.

### 프로젝트 로컬 설치
```
> git clone https://github.com/leeminseok8/diary.git

> cd --project_name
```

### 가상 환경 설치
> pipenv를 사용하였습니다.
```
프로젝트 최상위 디렉토리(Pipfile)에서 실행)
> pwd
~/.../diary


pipenv가 없으시다면)
> pip install pipenv

> pipenv shell


pipenv가 있으시다면)
> pipenv shell
```

### DB 생성
```
프로젝트 최상위 디렉토리(manage.py)에서 실행)
> pwd
~/.../diary

> python manage.py makemigrations

> python manage.py migrate
```

### 로컬(개발용) 서버 실행
```
> python manage.py runserver
```

<br>

---

## 사용 기술 스택
- back-end : Python, Django, DjangoRestFramework

- DataBase : MySQL

- formater : black

<br>

---

## MVP Service
> 유저(회원가입, 로그인)없이 일기장 기능만 구현하였습니다.

### 일기장
> 생성, 조회 : 누구나 사용할 수 있습니다. <br>
수정, 삭제 : 일기장의 비밀번호를 입력하면 사용할 수 있습니다.
- 생성
    - 일기장을 생성할 수 있습니다.
        - 제목, 내용, 비밀번호를 입력해야 합니다.<br>
        -> 비밀번호는 최소 6자 이상, 숫자 1개를 포함해야 하며, 암호화 된 현태로 저장됩니다.

        - 생성 시 기준 도시(서울)의 날씨가 등록됩니다.
- 조회
    - 생성된 일기장을 조회합니다.
        - 최신글 기준으로 20개의 일기장을 조회할 수 있습니다.
        - 스크롤을 내릴 때마다 중복되지 않는 20개를 호출합니다.
- 수정
    - 선택한 일기장을 수정할 수 있습니다.
        - 비밀번호만 일치하면 수정가 가능합니다.
        - 날씨는 수정할 수 없습니다.
- 삭제
    - 선택한 일기장을 삭제할 수 있습니다.
        - 비밀번호만 일치하면 삭제가 가능합니다.

<br>

---

## API 명세서
| Domain | endpoint | Method | 기능 | 권한 |
| --- | --- | --- | --- | --- |
| **Posts** |posts/ | POST | 일기장 생성 | - |
|  | posts/ | GET | 일기장 조회 | - |
|  | posts/id/ | PUT/PATCH | 일기장 수정 | 암호 입력 |
|  | posts/id/ | DELETE | 일기장 삭제 | 암호 입력 |

<br>

---

## 기능 명세서 및 분석

<br>

### 일기장 생성
<img width="956" alt="스크린샷 2022-10-02 오후 5 48 52" src="https://user-images.githubusercontent.com/93478318/193445995-a7247c84-b322-4e54-b8f1-b884601cb206.png">

- 일기장을 생성합니다.
- 일기장 생성 시 외부 API를 통해 도시(서울)의 현재 날씨를 생성합니다.<br>
-> [참조 API](https://www.weatherapi.com)

<br>

### 일기장 조회
<img width="872" alt="스크린샷 2022-10-02 오후 5 53 40" src="https://user-images.githubusercontent.com/93478318/193446244-1f674b05-c9d7-4703-8cc3-26c793c3a9ae.png">

- 작성된 게시글 중 최신 글 20개를 호출합니다. db가 수정되어도 중복되지 않는 글을 호출하기 위해 커서 페이지네이션으로 구현하였습니다.

<br>

### 일기장 수정
<img width="957" alt="스크린샷 2022-10-02 오후 6 28 22" src="https://user-images.githubusercontent.com/93478318/193447460-4b4c00e5-1952-4ffc-a7bc-2312bb01ae8e.png">

- 날씨를 제외한 일기장 제목, 내용을 수정할 수 있습니다.

<br>

### 일기장 삭제
> 삭제는 별도의 데이터를 제공하지 않습니다.
- 해당 id의 게시물을 삭제합니다.

<br>

---

## 구현 코드

<br>

### 비밀번호 검증 및 암호화
<img width="1187" alt="스크린샷 2022-10-02 오후 6 53 03" src="https://user-images.githubusercontent.com/93478318/193448276-bb9bcb5d-5165-494e-86f0-c1d15ecc3de0.png">

- 검증된 비밀번호는 암호화하여 저장하도록 함수를 구현하였습니다.
