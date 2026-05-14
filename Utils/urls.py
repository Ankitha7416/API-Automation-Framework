base_url = "https://mentorship-portal-backend-gddmbnfxgncpargc.canadacentral-01.azurewebsites.net"

login_url = f"{base_url}/auth/login"
get_employee_url = f"{base_url}/employees/"
create_mentor_url = f"{base_url}/mentors/mentors"
update_mentor_url = lambda mentor_id: f"{base_url}/mentors/mentors/{mentor_id}"
delete_mentor_url = lambda mentor_name: f"{base_url}/mentors/mentors/{mentor_name}"