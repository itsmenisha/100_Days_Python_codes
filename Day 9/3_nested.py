# Travel logue
travel_logue = [
    {
        "country": "france",
        "visits": 10,
        "cities": ["paris", "lille", "dijon"]
    },
    {
        "country": "india",
        "visits": 8,
        "cities": ["delhi", "mumbai", "kolkata", "chennai"]
    }
]


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_logue.append(new_country)


add_new_country("nepal", 2, ["kathmandu", "pokhara", "jhapa"])
print(travel_logue)
# city = {
#     {
#         "france": 7,
#         "bangladesh": 89,
#         "bhutan": 4,
#         "isral": 2
#     },
#     {
#         "france": 7,
#         "bangladesh": 89,
#         "bhutan": 4,
#         "isral": 2
#     }
# }
# peoples = {
#     "nisha": {"detail": [21, "cats"]},
#     "usha": [24, "dogs"]
# }
