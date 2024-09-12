def write_file(file_name, file_content):
    w_file = open(f"{file_name}.txt", mode='w', encoding='utf-8')
    w_file.write(file_content)
    w_file.close()

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as a_file:
        a_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding='utf-8') as r_file:
        return r_file.read()
