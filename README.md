# 👋 이름 추가 실습

이 저장소는 Git 협업 실습을 위한 공간입니다.  
아래 목록에 **자신의 이름**을 추가하는 PR을 만들어보세요!

---

## 참여자 목록

조항중
김규보


---

## 참여 방법

1. 이 저장소를 **Clone** 합니다.
   ```bash
   git clone <저장소 URL>
   ```
2. 자신의 이름으로 **브랜치**를 만듭니다.
   ```bash
   git switch -c add/<이름>
   
   or

   git checkout -b <이름>
   ```
3. `README.md`의 참여자 목록에 **자신의 이름**을 추가합니다.
4. 변경사항을 **Commit & Push** 합니다.
   ```bash
   git add README.md
   git commit -m "docs: 이름 추가 - <이름>"
   git push origin add/<이름>
   ```
5. GitHub에서 `main` 브랜치로 **Pull Request**를 보냅니다.

---

## Docker 실습

`docker/` 폴더에서 Docker Compose를 사용한 실습도 진행할 수 있습니다.

```bash
cd docker
docker compose up -d --build
```

자세한 내용은 [docker/README.md](docker/README.md)를 참고하세요.
