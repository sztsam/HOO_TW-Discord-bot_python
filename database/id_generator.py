import uuid


class id_generator:
    def __new__(cls, type: int):
        return str(eval(f"uuid.uuid{type}()"))[:-13].replace("-", "")
