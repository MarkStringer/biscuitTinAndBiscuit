import random
from datetime import datetime

def generate_social_media_request():
    formats = [
        "Video",
        "Blog",
        "Meme",
        "Joke",
        "Listicle",
        "A cartoon",
        "A Devil's project management dictionary",
        "War story"
    ]

    subject_categories = [
        "A book I've read",
        "An idea I have",
        "A thing",
        "A thing that happened to me"
    ]

    subject_areas = [
        "Agile",
        "The biscuit tin and the biscuit",
        "Commitment and consistency",
        "Projects are data",
        "Status transactions"
    ]

    attitudes = [
        "Angry",
        "Analytical",
        "Resigned",
        "Friendly - flyer Mark",
        "Amused"
    ]

    selected_format = random.choice(formats)
    selected_category = random.choice(subject_categories)
    selected_area = random.choice(subject_areas)
    selected_attitude = random.choice(attitudes)

    request = f"It requests a {selected_format}, about {selected_category}, about {selected_area}, with a {selected_attitude} tone."
    
    return request

def log_request_to_file(request):
    with open("socMediaRequests.log", "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{date}] {request}\n")

if __name__ == "__main__":
    request = generate_social_media_request()
    print(request)
    log_request_to_file(request)
