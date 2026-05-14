def login_payload():
    return {
        "email": "ramcharit.shukla@alignedautomation.com",
        "role": "Admin"
    }
def create_mentor_payload():
    return {
        "name": "Test Mentor",
        "email": "ayush.khare@alignedautomation.com",
        "function": "TSS",
        "no_of_members": 2,
        "members_name": [
            "Apurva Deore"
        ],
        "last_5_rating": "5,6",
        "status": "Active"
    }
def update_mentor_payload():
    return {
        "name": "Ayush Khare",
        "email": "ayush.khare@alignedautomation.com",
        "function": "TSS",
        "no_of_members": 1,
        "members_name": ["Apurva Deore"],
        "last_5_rating": "5,6",
        "status": "Active"
    }

