# while문 예시

treeHit = 0
while treeHit < 10:
    treeHit += 1
    # print("나무를 %d번 찍었습니다." % treeHit)
    # print("나무를 {0}번 찍었습니다.".format(treeHit))
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무 넘어갑니다!")