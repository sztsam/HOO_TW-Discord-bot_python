import traceback
import datetime


def error_handling(self, error: Exception, parameters=None):
    error_message = str(error)
    error_stack = traceback.format_exc()
    error_stack_partial = error_stack.split('\n')[1]
    error_hash = f"{error_message}-{error_stack_partial}"
    existing_error = self.errors.find_one({"hash": error_hash})
    skip_error = {
        "startsWith": ["connect"],
        "includes": ["AxiosError: Request failed"]
    }
    if any(error_hash.startswith(string) for string in skip_error["startsWith"]):
        return False
    if any(string in error_hash for string in skip_error["includes"]):
        return False

    if not existing_error:
        data = {
            "ticket_status": "created",
            "comment": "",
            "hash": error_hash,
            "message": error_message,
            "parameters": parameters,
            "stack": error_stack,
            "count": 1,
            "timestamp": datetime.datetime.now(),
        }
        result = self.errors.insert_one(data)
    else:
        self.errors.update_one(
            {"hash": error_hash},
            {"$inc": {"count": 1}}
        )
    return False if existing_error else {"id": result.inserted_id, "hash": error_hash}
