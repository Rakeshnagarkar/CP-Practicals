Practical 9
Reverse and Add 
The “reverse and add” method is simple: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.
 For example: 
195                  Initial number
591
 		—–
 786
 687
 —– 
1473
 		3741
 —– 
5214 
4125
 —– 
9339        Resulting palindrome 
In this particular case the palindrome ‘9339’ appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome. 
You must write a program that give the resulting palindrome and the number of iterations (additions) to compute the palindrome. 
You might assume that all tests data on this problem:
• will have an answer , 
• will be computable with less than 1000 iterations (additions), 
• will yield a palindrome that is not greater than 4,294,967,295.
 Input 
The first line will have a number N (0 < N ≤ 100) with the number of test cases, the next N lines will have a number P to compute its palindrome. 
Output 
For each of the N tests you will have to write a line with the following data : minimum number of iterations(additions) to get to the palindrome and the resulting palindrome itself separated by one space.
Sample Input 
3 
195 
265 
750 
Sample Output 
4 
9339 
5 
45254 
3 
6666











Program:
import java.util.Scanner;
public class Main {
    public static void main(String... args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); // Read the number of test cases
        for (int n = 0; n < N; n++) {
            long P = sc.nextLong();
            int iter = 0;
            while (!isPalindrome(P)) {
                P += reverseDigits(P);
                iter++;
            } System.out.printf("%d %d\n", iter, P);
        }
        sc.close();
    }
   // Function to reverse digits of a number
    private static long reverseDigits(long num) {
        long revNum = 0;
        while (num != 0) {
            revNum = revNum * 10 + num % 10;
            num = num / 10;
        } return revNum;
    }
    // Function to check whether the number is a palindrome or not
    private static boolean isPalindrome(long num) {
        String str = Long.toString(num);
        int len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - i - 1)) {
                return false;
            }  }
        return true;
    } 
}










Input:
3 
195 
265 
750 
Output: 
4 
9339 
5 
45254 
3 
6666

