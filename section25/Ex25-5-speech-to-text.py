'''
파일 명: Ex25-5-speech-to-text.py

OpenAI STT(speech to text)
    음성 파일을 텍스트로 변환하는 기술
'''

from openai import OpenAI, api_key

api_key=''
client = OpenAI(api_key=api_key)

def transcribe_audio(audio_file_path, language='ko'):

    transcript = None

    with open(audio_file_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model='whisper-1',  # 음성인식 모델
            file=audio_file,
            language=language
        )

        return transcript.text

# 실행코드
result = transcribe_audio('speech.mp3', language='en')
print('STT:', result)