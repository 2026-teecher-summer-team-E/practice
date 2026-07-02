# 🐍 FastAPI 실습

FastAPI 백엔드를 Docker Compose로 실행하고, 라우터를 추가해보는 실습입니다.

## 폴더 구조

```
docker/
├── Dockerfile
├── docker-compose.yml
├── README.md
└── app/
    ├── main.py          # FastAPI 진입점 (라우터 등록 위치)
    ├── requirements.txt
    └── routers/
        └── items.py     # 예시 라우터
```

## 실행 방법

```bash
cd docker
docker compose up -d --build
```

- `-d` : 백그라운드(detached) 모드로 실행
- `--build` : 이미지를 새로 빌드한 뒤 실행

- 서버 주소: http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## 라우터 추가 실습

1. `app/routers/` 안에 새 파일을 만듭니다 (예: `users.py`)

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": []}
```

2. `app/main.py`에 라우터를 등록합니다

```python
from fastapi import FastAPI
from routers import items, users  # ← 추가

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)  # ← 추가
```

3. 변경사항 반영

```bash
docker compose up -d --build
```

4. http://localhost:8000/docs 에서 새 엔드포인트 확인

## 컨테이너 종료

```bash
docker compose down
```
