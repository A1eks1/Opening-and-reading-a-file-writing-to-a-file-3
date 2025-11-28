def merge_files_by_line_count(output_filename, input_filenames, input_directory=""):
    files_data = []

    for filename in input_filenames:
        filepath = input_directory + filename
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        files_data.append({
            'name': filename,
            'line_count': len(lines),
            'content': lines
        })

    files_data.sort(key=lambda x: x['line_count'])

    with open(output_filename, 'w', encoding='utf-8') as output:
        for file in files_data:
            output.write(file['name'] + '\n')
            output.write(str(file['line_count']) + '\n')
            output.writelines(file['content'])
            if file['content'] and not file['content'][-1].endswith('\n'):
                output.write('\n')
            output.write('\n')


input_files = ["1.txt", "2.txt", "3.txt"]
merge_files_by_line_count(
"result.txt",
input_files,
"./")