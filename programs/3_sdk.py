class APIClient:

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def request(self, endpoint: str, method: str = "GET", payload: dict | None = None):

        print(f"[{method}] {self.base_url}/{endpoint}")

        if payload:
            print("Payload:", payload)

        return {
            "status": "success",
            "endpoint": endpoint,
            "data": payload
        }


class SDKClient:

    def __init__(self, base_url: str, api_key: str):
        self.client = APIClient(base_url, api_key)


    def create_user(self, name: str, email: str):
        payload = {
            "name": name,
            "email": email
        }

        return self.client.request(
            endpoint="users",
            method="POST",
            payload=payload
        )

    def get_user(self, user_id: int):
        return self.client.request(
            endpoint=f"users/{user_id}"
        )

    def update_user_email(self, user_id: int, new_email: str):
        payload = {
            "email": new_email
        }

        return self.client.request(
            endpoint=f"users/{user_id}",
            method="PUT",
            payload=payload
        )

    def delete_user(self, user_id: int):
        return self.client.request(
            endpoint=f"users/{user_id}",
            method="DELETE"
        )

    def create_project(self, name: str, owner_id: int):
        payload = {
            "name": name,
            "owner_id": owner_id
        }

        return self.client.request(
            endpoint="projects",
            method="POST",
            payload=payload
        )

    def list_projects(self):
        return self.client.request(
            endpoint="projects"
        )

if __name__ == "__main__":

    sdk = SDKClient(
        base_url="https://api.example.com",
        api_key="demo_key"
    )

    sdk.create_user("Alice", "alice@example.com")
    sdk.get_user(1)
    sdk.update_user_email(1, "alice_new@example.com")
    sdk.create_project("AI Documentation Tool", 1)
    sdk.list_projects()