def single_root_words(words, *other_words):
    same_words = []
    for oword in other_words:
        if words.lower() in oword.lower() or oword.lower() in words.lower():
            same_words.append(oword)
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
print(single_root_words('Interprinter', 'print', 'InTer', 'Solor', 'In'))