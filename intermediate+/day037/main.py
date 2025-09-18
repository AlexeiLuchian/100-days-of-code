import requests
from info import token, username
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
# pixela_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
# graph_params = {
#     "id": "learning",
#     "name": "Learning",
#     "unit": "minutes",
#     "type": "int",
#     "color": "kuro",
# }

headers = {
    "X-USER-TOKEN": token,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

now = datetime.datetime.now()
now_str = now.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/learning"
pixel_params = {
    "date": now_str,
    "quantity": "60",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{now_str}"
update_params = {
    "quantity": "90",
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

remove_pixel_endpoint = f"{post_pixel_endpoint}/20250917"
response = requests.delete(url=remove_pixel_endpoint, headers=headers)
print(response.text)