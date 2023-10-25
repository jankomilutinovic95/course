import requests

# payload = {"username": "kuce", "password": "pass"}
r = requests.get("https://httpbin.org/basic-auth/kuce/pass", auth=("kuce", "pass"))

# r_dict = r.json()

print(r.text)
# print(r_dict['form'])
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

