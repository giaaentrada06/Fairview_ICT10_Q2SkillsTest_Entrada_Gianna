# Dictionary containing with information
clubs = {
    "Marching Band": {
        "Description": "A club for students interested in music and marching performances.",
        "Meeting Time": "Tuesday and Wednesday 03:00–4:30 PM",
        "Location": "Band Room",
        "Club Moderator": "Mr. Emilio Alumno",
        "Number of Members": 30
    },

    "Glee Club": {
        "Description": "A singing club for vocal performance.",
        "Meeting Time": "Monday 03:00–05:00 PM",
        "Location": "High School Music Room",
        "Club Moderator": "Mr. Denver Martin",
        "Number of Members": 25
    },

    "Dance Club": {
        "Description": "A club for students who love dancing.",
        "Meeting Time": "Tuesday 03:00–05:00 PM",
        "Location": "Teatro Preciosa",
        "Club Moderator": "Mr. Alfred Cases",
        "Number of Members": 20
    },

    "Math Club": {
        "Description": "Enhances problem-solving and math skills.",
        "Meeting Time": "Monday 02:30–03:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Mr. Nicole Gabuya",
        "Number of Members": 15
    },

    "Science Club": {
        "Description": "Explores science through activities and experiments.",
        "Meeting Time": "Tuesday 03:00–04:00 PM",
        "Location": "Room 404",
        "Club Moderator": "Ms. Jameelyn Maramag",
        "Number of Members": 18
    },

    "Communications Arts Club": {
        "Description": "Develops speaking, writing, and media skills.",
        "Meeting Time": "Wednesday & Friday 03:00–04:00 PM",
        "Location": "Room 406",
        "Club Moderator": "Ms. Yannis Fernandez",
        "Number of Members": 22
    },

    "COCC": {
        "Description": "Military leadership and discipline training.",
        "Meeting Time": "Wednesday 02:30–04:30 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Club Moderator": "SSgt. Jemima David PA (Res)",
        "Number of Members": 35
    },

    "Social Science Club": {
        "Description": "Focuses on history, culture, and society.",
        "Meeting Time": "Tuesday 03:00–04:00 PM",
        "Location": "Room 409",
        "Club Moderator": "Mr. Roberto Lim",
        "Number of Members": 16
    },

    "Volleyball Varsity": {
        "Description": "Competitive volleyball training.",
        "Meeting Time": "Wednesday 03:00–04:00 PM",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 14
    },

    "Basketball Varsity": {
        "Description": "Competitive basketball training.",
        "Meeting Time": "Monday 03:00–04:00 PM",
        "Location": "Quadrangle",
        "Club Moderator": "Mr. Adrian Ruiz",
        "Number of Members": 14
    }
}

def display_club_info(club_name):
    print("Club Name:", club_name)
    for info in clubs[club_name]:
        print(info + ":", clubs[club_name][info])

display_club_info("Marching Band")
