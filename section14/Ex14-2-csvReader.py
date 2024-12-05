'''
파일 명: Ex14-2-csvReader.py

CSV(Comma-separated Values)
    필드를 쉼표(,)로 구분한 텍스트 데이터 파일
'''

member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break

        member = line.split(',')
        member_list.append(member)

print(member_list)











