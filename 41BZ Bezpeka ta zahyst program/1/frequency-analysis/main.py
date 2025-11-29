import collections

FREQUENT = "ОАИВНЕТСІРДЛМУПКГБЇЙЗЯЬХЖЧЮШЩЦЄФҐ"
REGULAR = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


org_text = "І повідкидав Йосія всю гидоту з усїх земель, що в синів Ізрайлевих; і приказав усїм, що знаходились в Ізраїлї, служити Господеві, Богові свойму. І за ввесь час живоття його не одступали вони від Господа, Бога отцїв своїх."
cph_text = "И мннжґщєґля Шлрцщ ноь азрлсд ж ррчт фглсїщ, ша б озяжб Жжвьїьгбхт; ж бнзщьжля доію, іл фкяєлґхїзгч н Ифнячїі, рьрєхпз Ангмнргбц, Млваяи обаилд. Ц жл бнгрї цло уєбапск їаан кд лґгптбькх бакз яир Ваооавя, Ааая лсжзб обазф."


def frequency_analysis(text: str, original_text: str = "", log_process: bool = False):
    clean_text = "".join(letter.upper() for letter in text if letter.isalpha())
    common_letters = [
        letter for letter, _ in collections.Counter(clean_text).most_common()
    ]
    print(common_letters)
    print(list(FREQUENT))

    """
    Співставляє найбільш використані літери наданого тексту (text)
    з найбільш популярними літерами алфавіту (FREQUENT)
    """
    mapping = dict(zip(common_letters, FREQUENT))

    new_text = str()
    for index, letter in enumerate(text):
        if letter.isalpha() and letter.upper() in mapping:
            new_letter = mapping[letter.upper()]
            new_letter = new_letter if letter == letter.upper() else new_letter.lower()
        else:
            new_letter = letter
        new_text += new_letter

        if log_process:
            try:
                print(f"{original_text[index]} was {letter} and is {new_letter}")
            except IndexError:
                print(f"{letter} is {new_letter}")

    return new_text


def calculate_error(deciphered_text: str, original_text: str):
    clean_deciphered = [letter for letter in deciphered_text if letter.isalpha()]
    clean_original = [letter for letter in original_text if letter.isalpha()]

    if not clean_original:
        return 0.0

    mismatches = sum(d != o for d, o in zip(clean_deciphered, clean_original))
    return mismatches / len(clean_original)


original_text = org_text
original_text = "Це текст"
print(original_text)

given_text = cph_text
given_text = "Їф шхуяш"
deciphered_text = frequency_analysis(given_text, original_text, True)
print(deciphered_text)

error = calculate_error(deciphered_text, original_text)
print(error)
