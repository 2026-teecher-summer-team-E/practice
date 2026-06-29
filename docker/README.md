# 🐳 Docker Compose 실습

nginx 웹 서버를 Docker Compose로 실행해보는 실습입니다.

## 폴더 구조

```
docker/
├── docker-compose.yml   # 서비스 정의
├── README.md            # 이 파일
└── app/
    ├── Dockerfile       # nginx 이미지 빌드 설정
    └── index.html       # 서빙할 웹 페이지
```

## 실습 순서

### 1. 컨테이너 빌드 & 백그라운드 실행

```bash
docker compose up -d --build
```

- `-d` : 백그라운드(detached) 모드로 실행
- `--build` : 이미지를 새로 빌드한 뒤 실행

### 2. 결과 확인

브라우저에서 아래 주소를 열어보세요.

```
http://localhost:8080
```

### 3. 실행 중인 컨테이너 확인

```bash
docker compose ps
```

### 4. 로그 확인

```bash
docker compose logs -f
```

### 5. 컨테이너 중지 & 삭제

```bash
docker compose down
```

## 추가 실습 아이디어

- `app/index.html`을 수정하고 `docker compose up -d --build`로 반영해보기
- `docker-compose.yml`에서 포트 번호를 바꿔보기 (`8080:80` → `9090:80`)
- `docker images` / `docker ps -a` 명령어로 이미지·컨테이너 목록 확인하기
