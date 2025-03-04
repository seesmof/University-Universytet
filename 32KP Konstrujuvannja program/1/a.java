import java.util.Scanner;

class a {
  public static boolean isNumberPalindrome(int number) {
    String stringNumber = Integer.toString(number);
    System.out.println(stringNumber);
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

    boolean palindromeNumberFound = false;
    int[] palindromeNumbers = new int[numberOfDigits];
    for (int i = 0; i < palindromeNumbers.length; i++) {
      int thisNumber = numbersArray[i];
      boolean isThisNumberPalindrome = isNumberPalindrome(thisNumber);
      if (isThisNumberPalindrome)
        palindromeNumberFound = true;
    }

    if (palindromeNumberFound) {
      System.out.println("Palindrome numbers:");
    }
  }
}