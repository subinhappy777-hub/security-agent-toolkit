def say_hello():
    print("안녕하세요")

say_hello()
say_hello()

def show_alert(user):
    print(f"{user} 계정을 확인하세요")

show_alert("kim01")
show_alert("park03")

def add(a,b):
    return a+b
result=add(3,5)
print(result)

logs=[
    {"result": "FAIL"}, {"result":"OK"},
    {"result": "FAIL"}, {"result":"FAIL"}
]

def count_failed(logs):
    fail_count=0
    for log in logs:
        if log["result"]=="FAIL":
            fail_count=fail_count+1
    return fail_count
total=count_failed(logs)
print(f"실패 {total}건")

def greet(name):
    print(f"안녕하세요 {name}")

greet("기찬")
greet("정민")