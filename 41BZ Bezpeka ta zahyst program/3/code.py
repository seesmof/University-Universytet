import os

def hide_lsb(input_path, output_path, text_message):
    try:
        # Відкриваємо файл для читання бінарних даних
        with open(input_path, 'rb') as f:
            bmp_header = f.read(54)  # Перші 54 байти - це заголовок
            image_data = bytearray(f.read()) # Решта - пікселі

        # Додаємо спеціальний стоп-символ (null-byte), щоб знати де кінець тексту
        message_bytes = text_message.encode('utf-8') + b'\x00'
        
        # Перевірка: чи вистачить місця (1 байт повідомлення = 8 байт картинки)
        if len(message_bytes) * 8 > len(image_data):
            print("Помилка: Зображення занадто мале для такого тексту!")
            return

        data_idx = 0 # Індекс байта картинки
        
        # Проходимо по кожному байту нашого повідомлення
        for byte in message_bytes:
            # Проходимо по кожному біту цього байта (від 0 до 7)
            for bit_pos in range(8):
                # Отримуємо значення біта (0 або 1)
                # зсуваємо байт і беремо останній біт
                bit = (byte >> bit_pos) & 1
                
                # Змінюємо байт картинки:
                # & 254 (11111110) - очищає останній біт
                # | bit - записує наш біт
                image_data[data_idx] = (image_data[data_idx] & 254) | bit
                
                data_idx += 1

        # Записуємо результат у новий файл
        with open(output_path, 'wb') as f:
            f.write(bmp_header)
            f.write(image_data)
            
        print(f"[ОК] Повідомлення успішно сховано у '{output_path}'")

    except FileNotFoundError:
        print(f"Помилка: Файл '{input_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def decode_lsb(image_path):
    # Функція для перевірки (читання повідомлення назад)
    try:
        with open(image_path, 'rb') as f:
            f.read(54) # Пропускаємо заголовок
            image_data = f.read()

        extracted_bytes = bytearray()
        current_byte = 0
        bit_count = 0

        for byte in image_data:
            # Витягуємо останній біт з байта картинки
            bit = byte & 1
            
            # Записуємо біт у наш поточний байт
            # (bit << bit_count) зсуває біт на потрібну позицію
            current_byte |= (bit << bit_count)
            
            bit_count += 1
            
            # Коли зібрали 8 біт (1 повний байт символу)
            if bit_count == 8:
                # Якщо зустріли нульовий байт - кінець повідомлення
                if current_byte == 0:
                    break
                
                extracted_bytes.append(current_byte)
                current_byte = 0
                bit_count = 0

        print(f"[Прочитано] Зміст повідомлення: {extracted_bytes.decode('utf-8')}")

    except Exception as e:
        print(f"Помилка читання: {e}")

# --- ГОЛОВНА ЧАСТИНА ---
if __name__ == "__main__":
    input_file = "input.bmp"
    output_file = "key.bmp"

    # Поставити поточну папку як стандартний шлях
    os.chdir(os.path.dirname(__file__))

    # ВАШЕ ПРІЗВИЩЕ ІМ'Я ПО-БАТЬКОВІ
    my_message = "Онищенко Олег Антонович"

    print("--- Python LSB Steganography ---")
    
    # 1. Ховаємо текст
    hide_lsb(input_file, output_file, my_message)
    
    # 2. Для перевірки одразу пробуємо прочитати з нового файлу
    if os.path.exists(output_file):
        decode_lsb(output_file)