# 게임 만들기 (어떤 게임이든 상관 없음)

## 개요

- 파이썬 인터프리터를 사용하는 게임을 만든다.
- 게임 내 구성요소들은 클래스의 인스턴스가 되도록 설정
	- ex) 퀴즈게임
		- 질문: class Question
		- 답변: class Answer
		- 사용자: class User
		- ...등등

## 필수조건

- 사용자에게 선택지를 알려주고, 입력이 들어오면 처리 후 다시 다른 선택지를 보여주도록 함
- 게임오버 조건이 있어야 함 (시간제한 / Life제한 등등...)
- 스코어 또는 타임어택 중 하나를 이용해 랭킹을 매김
- 게임이 끝난 후, 유저명과 점수를 파일에 저장
- 새 게임을 시작하면 파일에 저장되어있는 유저명과 점수를 이용해 탑 랭커 목록을 보여줌

## 제약사항

- 폴더명은 자신의 영문이름을 사용
- 메인 파일명은 game.py를 사용
	- leehanyeong/game.py
- 그 외 패키지나 모듈들은 얼마든지 추가해도 무관
	- leehanyeong/game.py
	- leehanyeong/functions/message.py
	- ...등등
- python game.py로 실행 시 동작하도록 한다.
- 이 프로젝트를 `fork`후, 작업이 완료되면 `pull request`를 보낸다. 다른 사람과 코드가 겹치지 않도록, root폴더를 기준으로 자신의 이름 폴더를 사용

## 작업 시 프로젝트 구조

```
<clone받아온 폴더>/
	<자신의 이름 폴더>/
		여기에 파일들 추가
```

```
# Example
Thansgiving-Homework/
	leehanyeong/
		main.py
		save_data/
			record.txt
		functions/
			__init__.py
			helper.py
```
