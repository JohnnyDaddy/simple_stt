windows 환경에서 pip install pyaudio 실행 중 에러가 발생하여 

https://pypi.org/project/PyAudio/#files 에서 PyAudio-0.2.14-cp312-cp312-win_amd64.whl 파일을 다운로드 받아 가상환경 생성 후 설치함.


# 가상환경 생성

```
python -m venv myenv
myenv\Scripts\activate
pip install SpeechRecognition
pip install PyAudio‑0.2.11‑cp312‑cp312‑win_amd64.whl
```

위의 과정에서 python 환경 변수 path가 MSYS2경로로 설정되어 있어 Scripts 디렉토리가 생성되지 않았으며

path 환경 변수를 windows version 설치 경로로 수정하여 해결함.
