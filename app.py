import speech_recognition as sr

# 음성 인식기 생성
r = sr.Recognizer()

# 마이크에서 음성을 듣고 텍스트로 변환
while True:
    with sr.Microphone() as source:
        print("말씀하세요...")
        audio = r.listen(source)

        try:
            # 한국어로 인식하려면 language='ko-KR'
            # r.adjust_for_ambient_noise(source)
            print("인식 중...")
            text = r.recognize_google(audio, language='ko-KR')
            print("인식된 내용:", text)
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print("Google 음성 인식 서비스에 접근할 수 없습니다:", e)
        except Exception as e:
            print("오류 발생:", e)