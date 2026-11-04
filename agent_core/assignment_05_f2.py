values=["2", "bad", "3"]
total=0

for i in values:
    try:
        total+=int(i)
    except ValueError:
        print("건너뜀", i)

print("합계", total)

try:
    n=int("abc")
    print(n)

except ValueError:
    print("숫자가 아닙니다")

print("프로그렘은 계속 돌아갑니다")

line="09:41,guest"
try:
    print(line[20])
except IndexError:
    print("칸이 모자랍니다, 확인 끝")


rows = [
    # ── 정상 17건 (칸 4개: 계정, IP, 결과, 실패횟수) ──
    "kim01,10.0.3.21,LOGIN_FAIL,5",
    "lee02,10.0.3.22,LOGIN_FAIL,2",
    "park03,10.0.3.23,LOGIN_OK,0",
    "choi04,10.0.3.24,LOGIN_FAIL,7",
    "han05,10.0.3.25,LOGIN_FAIL,1",
    "seo06,10.0.3.26,LOGIN_OK,0",
    "jung07,10.0.3.27,LOGIN_FAIL,3",
    "kang08,10.0.3.28,LOGIN_FAIL,6",
    "yoon09,10.0.3.29,LOGIN_OK,0",
    "lim10,10.0.3.30,LOGIN_FAIL,4",
    "oh11,10.0.3.31,LOGIN_FAIL,8",
    "shin12,10.0.3.32,LOGIN_OK,0",
    "kwon13,10.0.3.33,LOGIN_FAIL,2",
    "hwang14,10.0.3.34,LOGIN_FAIL,5",
    "ahn15,10.0.3.35,LOGIN_OK,0",
    "song16,10.0.3.36,LOGIN_FAIL,9",
    "ryu17,10.0.3.37,LOGIN_FAIL,1",
    # ── 깨진 5건 (칸이 4개 미만 → parts[3] 접근 시 IndexError) ──
    "broken01,10.0.3.40",
    "broken02",
    "broken03,10.0.3.42",
    "broken04",
    "broken05,10.0.3.44",
]

with open("sample_logs_broken.csv", "w", encoding="utf-8") as f:
    for r in rows:
        f.write(r + "\n")

with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        lines=line.strip().split(",")
        try:
            print(lines)
        except IndexError:
            print("pass")

ex1=0
broken_lines=[]
with open("sample_logs_broken.csv", encoding="utf-8") as f:
    for line in f:
        lines=line.strip().split(",")
        try:
            lines[3]
        except IndexError:
            broken_lines.append(line.strip())
            ex1+=1
print("깨진 줄 ",ex1,"가 담긴 리스트")
print(broken_lines)

"""time="??:??"
hour=int(time.split(":")[0])
print(hour)"""

line = "03:22,hacker,LOGIN_FAIL,10.0.9.9"
hour=int(line.split(":")[0])
print(hour)

if hour>=0 and hour<=6 :
    print("야간")