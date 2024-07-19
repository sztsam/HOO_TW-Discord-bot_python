def check_connect(self):
    try:
        return self.client.admin.command('ping')["ok"]
    except Exception as error:
        print(f"Connection error: {error}")
        return False
