import urllib.request

response = urllib.request.urlopen("https://placekitten.com/500/500")

cat_img = response.read()

with open("cat_600_600.jpg", "wb") as f:
    f.write(cat_img)
