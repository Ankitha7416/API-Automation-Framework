from Utils import variable

def get_headers():
    if variable.access_token:
        return {
            "Authorization": f"Bearer {variable.access_token}",
            "Content-Type": "application/json"
        }
    else:
        return {
            "Content-Type": "application/json"
        }
