class Admin:
    def __init__(self, admin_id: str, name: str, salt: bytes, hash: bytes):
        self.admin_id = admin_id
        self.name = name
        self.salt = salt
        self.hash = hash
