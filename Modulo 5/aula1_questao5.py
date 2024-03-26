import emoji

emojis_disponiveis = {
    ":grinning_face_with_big_eyes:": "\U0001F603",
    ":grinning_face_with_smiling_eyes:": "\U0001F604",
    ":grinning_face_with_sweat:": "\U0001F605",
    ":grinning_squinting_face:": "\U0001F606",
    ":winking_face:": "\U0001F609",
}

print("Emojis disponíveis:")
for codigo, emoji in emojis_disponiveis.items():
    print(codigo, "->", emoji)

frase_codificada = input(
    "Digite uma frase codificada usando os códigos de emoji acima: "
)

frase_emojizada = emoji.emojize(frase_codificada)
print("Sua frase emojizada é:", frase_emojizada)
