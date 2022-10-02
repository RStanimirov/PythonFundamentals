file_path_splitted = input().split('\\')

final_file = file_path_splitted[-1]
final_file_splitted = final_file.split('.')
file_extension = final_file_splitted[1]
file_name = final_file_splitted[0]

# print(file_path_splitted)
# print(final_file_splitted)
# print(final_file)
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")