import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = [
    ("ship1.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Oasis_of_the_Seas_in_Labadee%2C_Haiti.jpg/800px-Oasis_of_the_Seas_in_Labadee%2C_Haiti.jpg"),
    ("ship2.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Carnival_Breeze_in_Split.jpg/800px-Carnival_Breeze_in_Split.jpg"),
    ("ship3.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Queen_Mary_2_in_Sydney_Harbour.jpg/800px-Queen_Mary_2_in_Sydney_Harbour.jpg"),
    ("ship4.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Norwegian_Joy_%28ship%2C_2017%29_in_Kiel.jpg/800px-Norwegian_Joy_%28ship%2C_2017%29_in_Kiel.jpg"),
    ("ship5.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Costa_Smeralda_Savona_2019.jpg/800px-Costa_Smeralda_Savona_2019.jpg"),
    ("ship6.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/MSC_Grandiosa_in_Genoa.jpg/800px-MSC_Grandiosa_in_Genoa.jpg"),
    ("ship7.jpg", "https://images.unsplash.com/photo-1548574505-5e239809ee19?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
    ("ship8.jpg", "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
    ("ship9.jpg", "https://images.unsplash.com/photo-1572978332155-257a07525042?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
    ("ship10.jpg", "https://images.unsplash.com/photo-1505088214227-234f6d333066?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
    ("hero.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Oasis_of_the_Seas_in_Labadee%2C_Haiti.jpg/1920px-Oasis_of_the_Seas_in_Labadee%2C_Haiti.jpg")
]

os.makedirs('images', exist_ok=True)
print("Downloading images to local folder to ensure they load properly...")

for filename, url in images:
    filepath = os.path.join('images', filename)
    if not os.path.exists(filepath):
        try:
            print(f"Downloading {filename}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as response, open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
            # Fallback to placehold.co
            try:
                fallback_url = f"https://placehold.co/800x600/0077b6/ffffff.jpg?text={filename}"
                req = urllib.request.Request(fallback_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"Used placeholder for {filename}")
            except:
                print(f"Even placeholder failed for {filename}")
    else:
        print(f"{filename} already exists.")

print("All images downloaded successfully!")
