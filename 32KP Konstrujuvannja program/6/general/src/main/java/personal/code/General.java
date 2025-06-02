/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package personal.code;

import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

/**
 *
 * @author seesm
 */
public class General {

    static char upper(char givenCharacter) {
        return Character.toUpperCase(givenCharacter);
    }

    static char lower(char givenCharacter) {
        return Character.toLowerCase(givenCharacter);
    }

    static char convert(char givenCharacter) {
        return givenCharacter == lower(givenCharacter) ? upper(givenCharacter) : lower(givenCharacter);
    }

    public static void main(String[] args) {
        PrintStream out = new PrintStream(System.out, true, StandardCharsets.UTF_8);

        char[] alphabet = { 'А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н',
                'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я' };
        String alphabetString = new String(alphabet);
        out.println(alphabetString + ", кількість: " + alphabetString.length());
        for (int i = 0; i < alphabet.length; i++) {
            char letter = alphabet[i];
            out.println(letter + ": \\u" + Integer.toHexString(letter | 0x10000).substring(1) + ", decimal: "
                    + Character.codePointAt(alphabet, i) + ", converted: " + convert(letter));
        }
    }
}
