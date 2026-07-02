# FastAPI 백엔드 기초 실습 설계

## 목적

팀원들이 Git 협업 실습과 함께 FastAPI 라우터 추가 방법을 배울 수 있는 학습용 백엔드 환경을 구성한다.

## 범위

기존 `docker/` 폴더의 nginx 설정을 FastAPI 앱으로 교체한다. Docker Compose로 실행되며, 팀원들은 `routers/` 폴더에 파일을 추가하는 방식으로 실습한다.

## 디렉토리 구조

```
docker/
├── app/
│   ├── main.py              # FastAPI 앱 진입점, 라우터 등록
│   ├── routers/
│   │   └── items.py         # 예시 라우터
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 컴포넌트 상세

### main.py
- FastAPI 인스턴스 생성
- `routers/items.py` 라우터 등록 예시 포함
- 팀원이 자신의 라우터를 등록하는 위치

### routers/items.py (예시 라우터)
- `GET /items` — 전체 항목 목록 반환
- `POST /items` — 항목 추가
- 인메모리 리스트로 동작 (DB 불필요)

### Dockerfile
- `python:3.11-slim` 베이스 이미지
- `requirements.txt` 설치 후 `uvicorn`으로 앱 실행

### docker-compose.yml
- 포트 `8000:8000` 노출
- `docker compose up -d --build` 한 줄로 실행

### README.md
- FastAPI 실습 안내로 업데이트
- 라우터 추가 방법 단계별 설명

## 팀원 실습 흐름

1. `routers/` 안에 새 파일 생성 (예: `routers/users.py`)
2. `main.py`에 라우터 등록 한 줄 추가
3. `docker compose up -d --build`로 동작 확인
4. PR 제출

## 접근 방식

- 플랫 구조(라우터 파일 단위 분리)를 채택해 진입 장벽을 낮춤
- DB 없이 인메모리 데이터로 동작해 환경 설정 부담 없음
- `/docs` Swagger UI로 API 즉시 확인 가능
