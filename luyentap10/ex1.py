def get_file_with_ext(path):
    # Trích xuất "muabui.mp3"
    return path.split('\\')[-1]

def get_file_name_only(path):
    # Trích xuất "muabui"
    full_name = get_file_with_ext(path)
    return full_name.split('.')[0]

path = "d:\\music\\muabui.mp3"
print(get_file_with_ext(path))
print(get_file_name_only(path))
