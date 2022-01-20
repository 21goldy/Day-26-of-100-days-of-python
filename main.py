import pandas as p

logo = """
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗████████╗██╗ ██████╗    ███████╗ ██████╗ ██████╗ ███╗   ███╗███████╗
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔════╝
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗     ██║   ██║██║         █████╗  ██║   ██║██████╔╝██╔████╔██║███████╗
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝     ██║   ██║██║         ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║╚════██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗   ██║   ██║╚██████╗    ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                               
"""
file = p.read_csv("nato_phonetic_alphabet.csv")
data_frame = p.DataFrame(file)

# Printing logo
print(logo)

# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("\nEnter any word here: ").upper()
out_put = [phonetic_dict[letter] for letter in user_input]
print(f"\n{out_put}")
