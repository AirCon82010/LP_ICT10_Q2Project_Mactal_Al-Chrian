from pyscript import document

# Club data
clubs = {
    "DRAMA CLUB": {
        "Description": "Master the art of dramatic death scenes & tearful confessions.",
        "Meeting Time": "Mondays & Tuesdays & Wednesdays 3:45–5:30 PM",
        "Location": "Music Room",
        "Advisor": "Mr. Reyes",
        "Number of Members": "5",
        "Category": "Acting"
    },
    "MASTERMINDERS": {
        "Description": "Advanced scheming and complex plotting for long-term emotional damage.",
        "Meeting Time": "Thursdays & Fridays 4:00–5:15 PM",
        "Location": "Computer Lab",
        "Advisor": "Ms. Carabot",
        "Number of Members": "14",
        "Category": "Technology"
    },
    "ANTA-GONISTS": {
        "Description": "Perfecting the iconic villainous laugh and signature intimidating stare.",
        "Meeting Time": "Mondays & Fridays 3:30–4:30 PM",
        "Location": "Auditorium",
        "Advisor": "Ms. Solidum, Mr. Calixihan",
        "Number of Members": "22",
        "Category": "Student Development"
    },
    "CHAOS CREW": {
        "Description": "Specializing in explosive entrances, property damage, and disrupting happy endings.",
        "Meeting Time": "Tuesdays & Thursdays 3:00–4:15 PM",
        "Location": "Gymnasium",
        "Advisor": "Mr. De Leon",
        "Number of Members": "25",
        "Category": "Service & Operations"
    },
}

def show(club_name):
    info_box = document.getElementById("club_info_box")

    if club_name in clubs:
        details = clubs[club_name]
        text = f"Club Name: {club_name}\n"
        for k, v in details.items():
            text += f"{k}: {v}\n"
        info_box.innerText = text
    else:
        info_box.innerText = "No information available."

def Drama_Club(e):
    show("DRAMA CLUB")

def Master_Club(e):
    show("MASTERMINDERS")

def Anta_Club(e):
    show("ANTA-GONISTS")

def Chaos_Team(e):
    show("CHAOS CREW")