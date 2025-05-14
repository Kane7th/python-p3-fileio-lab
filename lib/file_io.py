def write_file(file_name="test_file", file_content="This is a test content." ):
    full_path = f"{file_name}.txt"
    with open(full_path, "w", encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name="test_file", append_content="This is a test append content."):
    full_path = f"{file_name}.txt"
    with open(full_path, "a", encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name="test_file"):
    full_path = f"{file_name}.txt"
    with open(full_path, "r", encoding='utf-8') as file:
        content = file.read()
    return content
