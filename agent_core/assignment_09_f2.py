def log(i):
    if i<3:
        print("기록 유지")
    else:
        print("추가 확인")

log(2)
log(3)

def start_check():
    print("점검을 시작합니다.")

start_check()
start_check()   

def show_user(user):
    print(user)

show_user("kim01")

def is_failed(result):
    if result=="FAIL":
        print("True")
    else:
        print("False")
is_failed("FAIL")

logs=[
    {"user":"kim01", "result":"FAIL"},
    {"user":"lee02", "result":"OK"},
    {"user":"park03", "result":"FAIL"},
]

def collect_failed_users(logs):
    failed_users=[]
    for log in logs:
        if log["result"]=="FAIL":
            failed_users.append(log["user"])
    return failed_users

print(collect_failed_users(logs))