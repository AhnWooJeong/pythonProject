'''
파일 명: Ex25-1-openai-api.py

OpenAI API 사용하기
    OpenAI에서 제공하는 AI(ChatGPT, DALL-E 등) 모델을 파이썬에서 활용

pip install openai

'''
from openai import OpenAI, api_key

api_key = ''

client = OpenAI(api_key=api_key)

'''
model: 사용할 AI 모델 지정
role: 
    system - AI 지시 또는 역할 부여 (페르소나 지정)
    user - 사용자
'''
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'system', 'content':'You are a helpful assistant.'},
        {
            'role':'user',
            'content':'이순신 업적 5가지'
        }
    ]
)

print(completion.choices[0].message.content)
'''
이순신은 조선 시대의 명장으로, 주로 임진왜란 동안의 업적으로 유명합니다. 그의 주요 업적 5가지는 다음과 같습니다.

1. **명량 해전**: 1597년 9월 16일, 이순신은 명량 해전에서 적군에 비해 훨씬 열세인 군세로 일본 수군을 상대로 결정적인 승리를 거두었습니다. 이 해전은 조선 수군의 사기를 높이고 일본의 해상 진출을 저지하는 중요한 전투가 되었습니다.

2. **한산도 대첩**: 1592년 7월 8일, 한산도에서 이순신은 일본 해군을 상대로 큰 승리를 거두었습니다. 이 전투에서는 '학익진'이라는 전술을 사용하여 적선을 효과적으로 무찌르고 수군의 우위를 확립했습니다.

3. **귀주 대첩**: 1592년, 이순신은 귀주에서 일본군을 상대로 선전하여 조선의 방어를 견고히 하였습니다. 이 전투에서 그의 지도력은 빛을 발하였습니다.

4. **철갑선 개발**: 이순신은 처음으로 철갑선을 개발하여 적의 포격에 견딜 수 있는 군함을 만들어 해전에서 큰 효과를 보았습니다. 이는 조선 수군의 전력 강화를 가져왔습니다.

5. **후국의 재건**: 이순신은 전투에서의 승리를 통해 조선의 군사적 기초를 다졌고, 전후에는 조선의 해상 안전을 보장하기 위한 여러 군사적 전략과 정책을 수립하여 국가의 재건에 기여하였습니다.

이러한 업적 덕분에 이순신은 한국 역사에서 가장 존경받는 인물 중 하나로 남아 있습니다.
'''














