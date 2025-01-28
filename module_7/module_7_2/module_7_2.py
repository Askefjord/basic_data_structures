def custom_write(file_name, strings):
    strings_position = {}
    file = open(file_name, 'w', encoding='utf-8')

    for text in range(len(strings)):
        strings_position[tuple([text + 1, file.tell()])] = strings[text]
        file.write(f'{strings[text]}\n')
    file.close()

    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

print(custom_write("output.txt", info))
