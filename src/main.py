import random, math


def derive_character_sheet(data: str) -> list[str]:
    character_sheet = []

    for char in data:
        if character_sheet.count(char) == 0:
            character_sheet.append(char)

    return character_sheet


def generate_data(seed: int, character_sheet: list[str], length: int) -> str:
    random.seed(seed)

    return random.choices(
        character_sheet,
        k=length,
    )


def crunch(data: str, chunk_size: int):
    data_length = len(data)

    loop_iterations = math.floor(data_length / chunk_size)
    loop_remainder = data_length % chunk_size

    for i in range(0, loop_iterations):
        data_window_start = i * chunk_size
        data_window_end = data_window_start + chunk_size

        target_data = data[data_window_start:data_window_end]

        character_sheet = derive_character_sheet(target_data)

    remainder_data = data[data_length - loop_remainder:data_length]
    remainder_character_sheet = derive_character_sheet(
        remainder_data
    )

    print(remainder_character_sheet)



with open("workspace/target.txt", "r") as file:
    crunch(
        file.read(),
        chunk_size=32
    )