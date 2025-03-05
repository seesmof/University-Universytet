import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class a {
  public static boolean isNumberPalindrome(int number) {
    String stringNumber = Integer.toString(number);
    String reversedNumber = "";

    for (int i = stringNumber.length() - 1; i >= 0; i--) {
      reversedNumber += stringNumber.charAt(i);
    }

    if (stringNumber.equals(reversedNumber))
      return true;
    else
      return false;
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

    System.out.println("\nPalindrome numbers:");
    for (int i = 0; i < palindromeNumbers.size(); i++) {
      System.out.println("- " + palindromeNumbers.get(i));
    }

    inputScanner.close();
  }
}