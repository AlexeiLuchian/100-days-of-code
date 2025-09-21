def update_info():
    import requests
    from info import AMADEUS_API_KEY, AMADEUS_API_SECRET

    amadeus_auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
    amadeus_cities_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    sheety_endpoint = "https://api.sheety.co/2896f611e30c5b6f2f226739242e2373/flightDeals/prices"

    sheety_response = requests.get(url=sheety_endpoint)
    sheety_response.raise_for_status()
    data = sheety_response.json()["prices"]

    cities = [row['city'] for row in data]
    iata_cities = []

    auth_headers = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET,
        "content-type": "application/x-www-form-urlencoded",
    }
    auth_response = requests.post(url=amadeus_auth_endpoint, data=auth_headers)
    access_token = auth_response.json()["access_token"]
    cities_headers = {
        "Authorization": f"Bearer {access_token}",
    }

    for city in cities:
        cities_params = {
            "keyword": city,
            "max": 1,
        }
        amadeus_response = requests.get(url=amadeus_cities_endpoint, params=cities_params, headers=cities_headers)
        amadeus_response.raise_for_status()
        city_data = amadeus_response.json()["data"]
        iata_cities.append(city_data[0]["iataCode"])

    sheety_put_endpoint = "https://api.sheety.co/2896f611e30c5b6f2f226739242e2373/flightDeals/prices"
    for row in range(2, len(iata_cities)+2):
        sheety_params = {
            "price": {
            "iataCode": iata_cities[row-2]
            }
        }
        response = requests.put(url=f"{sheety_put_endpoint}/{row}", json=sheety_params)
        response.raise_for_status()
