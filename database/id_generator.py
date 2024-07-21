import uuid


class id_generator:
    def __new__(cls, type: int) -> str:
        return str(eval(f"uuid.uuid{type}()"))[:-13].replace("-", "")
