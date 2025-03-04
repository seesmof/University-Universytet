import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class a {
  public static boolean isNumberPalindrome(int number) {
    String stringNumber = Integer.toString(number);
    System.out.println(stringNumber);

    String reversedNumber = "";
    for (int reverseCounter = stringNumber.length(), counter = 0; reverseCounter >= 0
        && counter < stringNumber.length(); reverseCounter--, counter++) {

    }
  }

  public static void main(String[] args) {
    Scanner inputScanner = new Scanner(System.in);

    System.out.print("Please enter N, number of digits: ");
    int numberOfDigits = inputScanner.nextInt();

    int[] numbersArray = new int[numberOfDigits];
    for (int i = 0; i < numbersArray.length; i++) {
      int readableNumber = i + 1;
      System.out.print("Please enter digit number " + readableNumber + ": ");
      int thisNumber = inputScanner.nextInt();
      numbersArray[i] = thisNumber;
    }

    List<Integer> palindromeNumbers = new ArrayList<Integer>();
    for (int i = 0; i < numbersArray.length; i++) {
      int thisNumber = numbersArray[i];
      boolean isThisNumberPalindrome = isNumberPalindrome(thisNumber);
      if (isThisNumberPalindrome)
        palindromeNumbers.add(thisNumber);
    }

    System.out.println("Palindrome numbers:");
    for (Integer thisNumber : palindromeNumbers) {
      System.err.println(thisNumber);
    }
  }
}