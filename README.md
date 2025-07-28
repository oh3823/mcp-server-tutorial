# 프로젝트 환경 설정 방법

이 문서는 저장소를 클론한 후 프로젝트를 정상적으로 실행하기 위한 환경 설정 방법을 안내합니다.

## 1. 저장소 클론

먼저, 터미널에서 아래 명령어로 저장소를 클론합니다.

```bash
git clone https://github.com/oh3823/mcp-server-tutorial.git
cd mcp-server-tutorial
```

## 2. Python 버전 확인

이 프로젝트는 **Python 3.12 이상**에서 동작합니다. 아래 명령어로 Python 버전을 확인하세요.

```bash
python --version
```

## 3. uv 설치

[uv](https://github.com/astral-sh/uv)는 Python 패키지 관리와 가상환경 생성을 빠르고 효율적으로 도와주는 도구입니다. 기존의 pip, venv, pip-tools 등을 대체하여 더 빠른 속도로 의존성 설치와 환경 구성을 할 수 있습니다.

uv는 아래 공식 문서를 참고하여 전역으로 설치하는 것을 권장합니다.

- [uv 공식 설치 가이드](https://docs.astral.sh/uv/getting-started/installation/)

설치가 완료되면 아래 명령어로 정상적으로 설치되었는지 확인할 수 있습니다.

```bash
uv --version
```

## 4. 가상환경 생성 및 활성화 (권장)

가상환경을 사용하면 프로젝트별로 패키지 관리를 할 수 있습니다.

```bash
# uv로 가상환경 생성
uv venv

# 또는 python 내장 venv 사용
python -m venv .venv

# Windows에서 가상환경 활성화
.venv\Scripts\activate

# macOS/Linux에서 가상환경 활성화
source .venv/bin/activate
```

## 5. 의존성 패키지 설치

`pyproject.toml`과 `uv.lock` 파일을 기반으로 의존성을 설치합니다.  
uv를 사용하는 경우 아래 명령어를 실행하세요.

```bash
uv pip install -r requirements.txt
```

> **참고:** `requirements.txt` 파일이 없는 경우, `pyproject.toml`을 참고하여 필요한 패키지를 직접 설치하세요.

## 6. 환경 변수 설정 (필요한 경우)

특정 API 키나 환경 변수가 필요한 경우, 프로젝트 루트에 `.env` 파일을 생성하여 환경변수를 설정하세요.

```env
# 예시
OPENAI_API_KEY=<YOUR_API_KEY>
GOOGLE_API_KEY=<YOUR_API_KEY>
```

## 7. 프로젝트 실행

설정이 완료되면 아래 명령어로 프로젝트를 실행할 수 있습니다.

```bash
uv run main.py
```

---
