count=int("7")
print(count+1)

count2=7
print("실패"+str(count2)+"회")
print(f"실패 {count2}회")

row ="kim01, 10.0.3 21,5"
parts=row.split(",")
fail_count=int(parts[2])
if fail_count>5:
    print("차단 대상")

temp="21:30"
hour=int(temp.split(":")[0])
print(hour)

raw="7"
try:
    print(int(raw))
except ValueError:
    print("숫자를 확인하세요")

ex="abc"

try:
    print(int(ex))
except ValueError:
    print("숫자가 아닙니다")
    print("확인 끝")