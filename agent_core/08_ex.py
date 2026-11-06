user={"name":"kim01", "dept": "finance", "level": "read"}
print(user["name"])
print(user["dept"])

user={"name":"kim01", "level": "read"}
user["level"]="admin"
user["approver"]="hr_mgr"
print(user)

log={
    "time": "2026-09-22 14:03:11",
    "user":"kim01",
    "ip":"10.0.3.21",
    "action" : "LOGIN",
    "result":"FAIL"
}
print(log["user"], log["result"])

log={"name":"kim01", "result": "FAIL"}
print(log.get("ip"))
print(log.get("ip", "알 수 없음"))
print("검사 완료")

log={"name":"kim01", "result": "FAIL"}
print(f"계정 {log['name']} IP{log.get('ip', '-')} RESULT{log['result']}")

books=[
    {"title":"파이썬", "price":20000},
    {"title":"네트워크","price":25000} 
]
print(books[0])
print(books[0]["title"])
print(books[1]["price"])

stores={
    "seoul":{"count":12, "open":True},
    "busan":{"count":5, "open":False}
}

print(stores["seoul"])
print(stores["seoul"]["count"])
stores["daegu"]={"count":3, "open":True}

alerts=[
    {"rule": "brute_force", "user":"admin", "tegs":["야간", "실패"]},
    {"rule": "night_login", "user":"lee02", "tags":["야간"]}
]

print(len(alerts),"건")

import json

menu={"name":"coffee", "price":4500}
text=json.dumps(menu)
print(text)

back=json.loads(text)
print(back["price"])

import json

menu={"name":"coffee", "price":4500}

with open("menu.json", "w", encoding="utf-8") as f:
    json.dump(menu, f, ensure_ascii=False, indent=2)

with open("menu.json", encoding="utf-8") as f:
    beck =json.load(f)

print(back["name"])
