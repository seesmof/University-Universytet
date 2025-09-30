import collections

FREQUENT = "ОАИВНЕТСІРДЛМУПКГБЇЙЗЯЬХЖЧЮШЩЦЄФҐ"
REGULAR = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


org_text = "І повідкидав Йосія всю гидоту з усїх земель, що в синів Ізрайлевих; і приказав усїм, що знаходились в Ізраїлї, служити Господеві, Богові свойму. І за ввесь час живоття його не одступали вони від Господа, Бога отцїв своїх."
cph_text = "И мннжґщєґля Шлрцщ ноь азрлсд ж ррчт фглсїщ, ша б озяжб Жжвьїьгбхт; ж бнзщьжля доію, іл фкяєлґхїзгч н Ифнячїі, рьрєхпз Ангмнргбц, Млваяи обаилд. Ц жл бнгрї цло уєбапск їаан кд лґгптбькх бакз яир Ваооавя, Ааая лсжзб обазф."

clean_text = cph_text.upper().replace(" ", "")
common_letters = [
    letter for letter, number in collections.Counter(clean_text).most_common()
]
cut_alphabet = list(FREQUENT[: len(common_letters)])
data = dict(zip(common_letters, cut_alphabet))
print(f"{common_letters = }")
print(f"{cut_alphabet = }")
print(f"{data = }")

new_text = str()
for index, letter in enumerate(cph_text):
    if letter.isalpha() and letter.upper() in data.keys():
        new_letter = data[letter.upper()]
        new_letter = new_letter if letter == letter.upper() else new_letter.lower()
    else:
        new_letter = letter
    new_text += new_letter
    print(f"{org_text[index]} was {letter} and is {new_letter}")
print(new_text)

error_amount = sum(
    letter != org_letter for letter, org_letter in zip(new_text, org_text)
) / len(org_text)
print(error_amount)
