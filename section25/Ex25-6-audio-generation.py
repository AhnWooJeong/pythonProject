'''
파일 명: Ex25-6-audio-generation.py

OpenAI Multimodal API - 텍스트와 음성 동시 생성
'''

import base64
from openai import OpenAI, completions

api_key=''

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model='gpt-4o-audio-preview',
    modalities=['text', 'audio'],
    audio={'voice': 'echo', 'format':'wav'},
    messages=[
        {'role':'user', 'content':'세종대왕 업적 5개 나열해줘'}
    ]
)

print(completion.choices[0].message.content)

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open('kingsejong.wav', 'wb') as file:
    file.write(wav_bytes)




