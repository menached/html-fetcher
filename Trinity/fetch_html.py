import requests
import time

# Fetch page 1
url = "https://trinityrealestatenicaragua.com/advanced-search/?filter_search_type%5B0%5D&advanced_contystate&advanced_city&property_status&bedrooms&bathrooms&keyword&price_low=0&price_max=2000000&submit=Search&elementor_form_id=46497"
filename = "page1.html"
response = requests.get(url)
with open(f"fetched/Trinity/{filename}", "wb") as file:
    file.write(response.content)

# Fetch pages 2 to 20
for i in range(2, 21):
    url = f"https://trinityrealestatenicaragua.com/advanced-search/page/{i}/?filter_search_type%5B0%5D&advanced_contystate&advanced_city&property_status&bedrooms&bathrooms&keyword&price_low=0&price_max=2000000&submit=Search&elementor_form_id=46497"
    filename = f"page{i}.html"
    response = requests.get(url)
    time.sleep(10)
    print(filename)
    with open(f"fetched/Trinity/{filename}", "wb") as file:
        file.write(response.content)
