/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package personal.individual;

import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

/**
 *
 * @author seesm
 */
public class Individual {
    static void identify(int k) {
        switch ((10000 < k && k <= 5) ? 1
                : (0 <= k && k <= 10) ? 2
                        : (5 <= k && k <= 15) ? 3
                                : (10 <= k && k <= 10000) ? 4
                                        : 5) {
            case 1 ->
                System.out.println(k + " belongs to (-10k, 5]");
            case 2 ->
                System.out.println(k + " belongs to [0, 10]");
            case 3 ->
                System.out.println(k + " belongs to [5, 15]");
            case 4 ->
                System.out.println(k + " belongs to [10, 10k]");
            case 5 ->
                System.out.println(k + " is out of range");
        }
    }

    public static void main(String[] args) {
        identify(7);
        identify(15);
        identify(54);
        identify(12857);
        
        PrintStream out = new PrintStream(System.out, true, StandardCharsets.UTF_8);
        out.println("Спаси Ісусе");
    }
}
