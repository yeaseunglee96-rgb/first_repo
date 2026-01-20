title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.

my_dict_1 = {
    '과목': 'Python', 
    '구분': '실습', 
    '단계': 2, 
    '문제번호': 3251, 
    '이름': None, 
    '일자': 22
}
print(my_dict_1)

my_dict_1['단계'] = str(my_dict_1['단계']) + '단계'
# print("2" + "단계")

my_dict_1['이름'] = title

my_dict_1['일자'] = my_dict_1['일자'] - 20


print(my_dict_1)