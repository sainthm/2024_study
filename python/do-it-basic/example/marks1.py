# marks1.py
# 총 5명의 학생이 시험을 보았습니다.
# 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격입니다.
# 학생들의 시험 결과가 합격인지 불합격인지 결과를 보여주시오.
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")