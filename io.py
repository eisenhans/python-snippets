import requests, zipfile, io

# zip extrahieren
r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()