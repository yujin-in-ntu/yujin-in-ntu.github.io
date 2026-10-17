# Yujin Lee — personal website

빌드 도구 없는 정적 사이트입니다. `index.html`(내용)과 `style.css`(디자인) 두 파일이 전부입니다.

## 1. GitHub에 올리기 (처음 한 번)

1. 유진님 GitHub 계정으로 로그인해서 **새 repository**를 만듭니다.
   - 이름은 반드시 `<GitHub아이디>.github.io` (예: 아이디가 `yujinlee`면 `yujinlee.github.io`)
   - Public, README 추가 체크 해제
2. 이 폴더 이름도 같게 맞추고(선택), 터미널에서:

```bash
git add -A && git commit -m "Initial site"
git remote add origin https://github.com/<GitHub아이디>/<GitHub아이디>.github.io.git
git push -u origin main
```

3. repo → **Settings → Pages** → Source: `Deploy from a branch`, Branch: `main` / `(root)` → Save
4. 1~2분 뒤 `https://<GitHub아이디>.github.io` 에서 열립니다.

## 2. 내용 채우기

`index.html`에서 `[대괄호]`와 `TODO` 주석이 있는 곳만 바꾸면 됩니다.

| 바꿀 것 | 위치 |
|---|---|
| 프로필 사진 | `images/profile-2.jpg`, `images/profile-3.jpg` (정사각형 권장). 2장 이상이면 돌아가며 넘어감. 더 넣으려면 index.html 의 avatar 안에 `<img>` 추가 |
| 시샤 | `images/shisa.png` (투명 배경 PNG) 넣으면 사진 옆에 앉음 |
| CV | `cv.pdf` 를 루트에 넣고 index.html 의 CV 링크 주석 풀기 |
| 이메일 / Scholar / GitHub / ORCID | 왼쪽 `<ul class="links">` |
| 논문 | 주석 처리된 Publications 섹션 주석 풀고 채우기 |
| 뉴스 | `<ul class="news">` 맨 위에 한 줄 추가 |
| 색 | `style.css` 맨 위 `--accent` (지금은 더스티 로즈) |

수정 후 `git add -A && git commit -m "update" && git push` 하면 1분 안에 반영됩니다.
GitHub 웹에서 파일 열고 연필 아이콘으로 바로 고쳐도 됩니다.

## 3. 확인용 단일 파일 만들기

```bash
python3 build_preview.py
```

사진까지 다 들어간 `../yujinlee-site-preview.html` 이 생깁니다.

## 4. 로컬에서 미리보기

```bash
python3 -m http.server 8000
```

브라우저에서 http://localhost:8000
