poznachky = """
Flask – бібліотека розробки серверної частини застосунку
JavaScript – мова програмування веб-застосунків
NextJS – фреймворк розробки клієнтської частини застосунку
Python – високорівнева мова програмування з динамічною типізацією
TailwindCSS – сучасна бібліотека стилізації веб-сторінок
""".strip()

sorted_poznachky = sorted(poznachky.split("\n"))
united_poznachky = "\n".join(sorted_poznachky)

print(united_poznachky)
