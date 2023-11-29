import uuid


def generate_file_name() -> str:
    base = uuid.uuid4()
    return str(base)[:8]
