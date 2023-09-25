#!/bin/bash
#Fetch Discover SJDS Pages
#get page 1
    url="https://discoversjds.com/property-search/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
    filename="page1.html"
    curl -o "current/$filename" "$url"

# Fetch pages 2 to 20
for i in {2..20}
do
    url="https://discoversjds.com/property-search/page/${i}/?keyword&location=any&status=any&type=any&bedrooms=any&bathrooms=any&min-price=any&max-price=any&min-area&max-area"
    filename="page${i}.html"
    curl -o "current/$filename" "$url"
done
