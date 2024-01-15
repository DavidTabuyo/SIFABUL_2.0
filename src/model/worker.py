class Worker:
    def __init__(self, worker_id: str, name: str, salt: bytes, hash: bytes, admin_id: str):
        self.worker_id = worker_id
        self.name = name
        self.salt = salt
        self.hash = hash
        self.admin_id = admin_id

    def get_output_for_list(self) ->str:
        return self.worker_id+": "+self.name
    
    def getID(self) ->str:
        return self.worker_id
