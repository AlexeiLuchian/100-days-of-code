import requests
from info import token, username

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
graph_params = {
    "id": "learning",
    "name": "Learning",
    "unit": "minutes",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": token,
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)