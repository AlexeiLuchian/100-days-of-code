def search_cheaper_flights():
    import requests
    from info import AMADEUS_API_KEY, AMADEUS_API_SECRET, MY_IATA_LOCATION
    import datetime as dt
    from send_message import send_message
    from sheet_management import update_info

    update_info()

    sheety_endpoint = "https://api.sheety.co/2896f611e30c5b6f2f226739242e2373/flightDeals/prices"
    amadeus_auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
    amadeus_offers_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers?"
    sheety_put_endpoint = "https://api.sheety.co/2896f611e30c5b6f2f226739242e2373/flightDeals/prices"

    auth_headers = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET,
        "content-type": "application/x-www-form-urlencoded",
    }
    auth_response = requests.post(url=amadeus_auth_endpoint, data=auth_headers)
    access_token = auth_response.json()["access_token"]
    amadeus_headers = {
        "Authorization": f"Bearer {access_token}",
    }

    sheety_response = requests.get(url=sheety_endpoint)
    sheety_response.raise_for_status()
    data = sheety_response.json()['prices']
    prices_dict = {item["iataCode"]:item["lowestPrice"] for item in data}
    id_dict = {item["iataCode"]:item["id"] for item in data}

    today = dt.datetime.today()
    tomorrow = today + dt.timedelta(days=1)
    six_month_from_tomorrow = tomorrow + dt.timedelta(days=90)
    six_month_from_tomorrow_str = six_month_from_tomorrow.strftime("%Y-m-%d")
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")


    for flight in prices_dict:
        amadeus_params = {
            "originLocationCode": MY_IATA_LOCATION,
            "destinationLocationCode": flight,
            "departureDate": (tomorrow_str,six_month_from_tomorrow_str),
            "adults": 1,
        }
        amadeus_offer = requests.get(url=amadeus_offers_endpoint, params=amadeus_params, headers=amadeus_headers)
        amadeus_offer.raise_for_status()
        amadeus_offer_data = amadeus_offer.json()["data"]

        for offer in amadeus_offer_data:
            if float(offer["price"]["total"]) < prices_dict[flight]:
                sheety_params = {
                    "price": {
                    "lowestPrice": offer["price"]["total"],
                    }
                }
                sheety_response = requests.put(url=f"{sheety_put_endpoint}/{id_dict[flight]}", json=sheety_params)

                message = f"We found a better offer for your {MY_IATA_LOCATION} - {flight} flight on {offer["itineraries"][0]["segments"][0]["departure"]["at"]} for the price of {offer["price"]["total"]} {offer["price"]["currency"]}."
                print(message)
                send_message(message=message)