# FastAPI 백엔드 기초 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 기존 `docker/` 폴더의 nginx 설정을 FastAPI 앱으로 교체하고, 팀원들이 라우터를 추가하며 실습할 수 있는 환경을 구성한다.

**Architecture:** `docker/app/` 안에 FastAPI 소스(main.py + routers/)를 두고, `docker/` 루트의 Dockerfile이 이를 빌드한다. docker-compose.yml이 포트 8000으로 서비스를 노출하며, 팀원은 `routers/` 폴더에 파일을 추가하고 main.py에 등록하는 방식으로 실습한다.

**Tech Stack:** Python 3.11, FastAPI, uvicorn, Docker, Docker Compose

## Global Constraints

- Python 버전: 3.11-slim 이미지 사용
- 포트: 8000 (호스트 8000 → 컨테이너 8000)
- DB 없음: 인메모리 리스트로만 동작
- `docker compose up -d --build` 한 줄로 실행 가능해야 함
- 기존 `docker/app/Dockerfile`, `docker/app/index.html` 삭제

---

## 파일 맵

| 상태 | 경로 | 역할 |
|------|------|------|
| 삭제 | `docker/app/Dockerfile` | 기존 nginx Dockerfile |
| 삭제 | `docker/app/index.html` | 기존 nginx 페이지 |
| 생성 | `docker/Dockerfile` | Python/FastAPI 빌드 |
| 생성 | `docker/app/requirements.txt` | 의존성 목록 |
| 생성 | `docker/app/main.py` | FastAPI 앱 진입점 |
| 생성 | `docker/app/routers/__init__.py` | 패키지 초기화 |
| 생성 | `docker/app/routers/items.py` | 예시 라우터 |
| 수정 | `docker/docker-compose.yml` | 빌드 컨텍스트·포트 변경 |
| 수정 | `docker/README.md` | FastAPI 실습 안내로 업데이트 |

---

## Task 1: 브랜치 생성 및 nginx 파일 제거

**Files:**
- Delete: `docker/app/Dockerfile`
- Delete: `docker/app/index.html`

- [ ] **Step 1: 새 브랜치 생성**

```bash
git switch -c add/fastapi-backend
```

Expected: `Switched to a new branch 'add/fastapi-backend'`

- [ ] **Step 2: 기존 nginx 파일 삭제**

```bash
git rm docker/app/Dockerfile docker/app/index.html
```

Expected: `rm 'docker/app/Dockerfile'` / `rm 'docker/app/index.html'`

- [ ] **Step 3: 커밋**

```bash
git commit -m "chore: nginx 파일 제거"
```

---

## Task 2: Dockerfile과 requirements.txt 작성

**Files:**
- Create: `docker/Dockerfile`
- Create: `docker/app/requirements.txt`

**Interfaces:**
- Produces: `docker build .` 성공, `fastapi`, `uvicorn[standard]` 설치됨

- [ ] **Step 1: requirements.txt 작성**

`docker/app/requirements.txt`:
```
fastapi==0.111.0
uvicorn[standard]==0.29.0
```

- [ ] **Step 2: Dockerfile 작성**

`docker/Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 3: 빌드 테스트**

```bash
cd docker && docker build -t fastapi-test .
```

Expected: `Successfully built ...` (에러 없이 종료)

- [ ] **Step 4: 커밋**

```bash
git add docker/Dockerfile docker/app/requirements.txt
git commit -m "feat: Dockerfile 및 requirements.txt 추가"
```

---

## Task 3: docker-compose.yml 업데이트

**Files:**
- Modify: `docker/docker-compose.yml`

**Interfaces:**
- Consumes: Task 2에서 생성한 `docker/Dockerfile`
- Produces: `docker compose up -d --build` 실행 시 포트 8000으로 서비스 실행

- [ ] **Step 1: docker-compose.yml 교체**

`docker/docker-compose.yml`:
```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    restart: unless-stopped
```

- [ ] **Step 2: compose 설정 검증**

```bash
cd docker && docker compose config
```

Expected: 에러 없이 정규화된 설정 출력

- [ ] **Step 3: 커밋**

```bash
git add docker/docker-compose.yml
git commit -m "feat: docker-compose.yml을 FastAPI용으로 업데이트"
```

---

## Task 4: FastAPI 앱 파일 작성

**Files:**
- Create: `docker/app/main.py`
- Create: `docker/app/routers/__init__.py`
- Create: `docker/app/routers/items.py`

**Interfaces:**
- Consumes: Task 2의 `requirements.txt` (fastapi, uvicorn)
- Produces:
  - `GET /items` → `{"items": [...]}`
  - `POST /items` body `{"name": str}` → `{"name": str}` 추가 후 목록 반환
  - `GET /docs` → Swagger UI

- [ ] **Step 1: routers/__init__.py 생성 (빈 파일)**

`docker/app/routers/__init__.py`:
```python
```

- [ ] **Step 2: 예시 라우터 작성**

`docker/app/routers/items.py`:
```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

items = []


class Item(BaseModel):
    name: str


@router.get("/items")
def get_items():
    return {"items": items}


@router.post("/items")
def create_item(item: Item):
    items.append(item.name)
    return {"items": items}
```

- [ ] **Step 3: main.py 작성**

`docker/app/main.py`:
```python
from fastapi import FastAPI
from routers import items

app = FastAPI()

app.include_router(items.router)
```

- [ ] **Step 4: 컨테이너 실행 및 동작 확인**

```bash
cd docker && docker compose up -d --build
```

Expected: `Container ... Started`

- [ ] **Step 5: 엔드포인트 검증**

```bash
# 목록 조회
curl http://localhost:8000/items
```
Expected: `{"items":[]}`

```bash
# 항목 추가
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "apple"}'
```
Expected: `{"items":["apple"]}`

```bash
# 목록 재조회
curl http://localhost:8000/items
```
Expected: `{"items":["apple"]}`

브라우저에서 `http://localhost:8000/docs` 접속 → Swagger UI 확인

- [ ] **Step 6: 컨테이너 종료**

```bash
cd docker && docker compose down
```

- [ ] **Step 7: 커밋**

```bash
git add docker/app/main.py docker/app/routers/
git commit -m "feat: FastAPI 앱 및 예시 라우터(items) 추가"
```

---

## Task 5: README.md 업데이트

**Files:**
- Modify: `docker/README.md`

- [ ] **Step 1: README.md 교체**

`docker/README.md`:
```markdown
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
```

- [ ] **Step 2: 커밋**

```bash
git add docker/README.md
git commit -m "docs: FastAPI 실습 안내로 README 업데이트"
```
