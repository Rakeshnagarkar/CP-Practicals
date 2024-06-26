Practical 8
Primary Arithmetic
 Children are taught to add multi-digit numbers from right-to-left one digit at a time. Many find the “carry” operation - in which a 1 is carried from one digit position to be added to the next - to be a significant challenge. Your job is to count the number of carry operations for each of a set of addition problems so that educators may assess their difficulty. 
Input
 Each line of input contains two unsigned integers less than 10 digits. The last line of input contains ‘0 0’.
Output
 For each line of input except the last you should compute and print the number of carry operations that would result from adding the two numbers, in the format shown below. 
Sample Input 
123 456 
555 555 
123 594
 0 0 
Sample Output 
No carry operation. 
3 carry operations. 
1 carry operation.







Program:





import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNext()) {
            long x = scanner.nextLong();
            long y = scanner.nextLong();
            int step = 0;
            if (x == 0 && y == 0) break;
            else {
                int temp = 0;
                while (x != 0 || y != 0) {
                    if (x % 10 + y % 10 + temp >= 10) {
                        step++;
                        temp = 1;
                    } else {
                        temp = 0;
                    }
                    x /= 10;  y /= 10;
                }
            }
            if (step == 0) {
                System.out.println("No carry operation.");
            } else if (step == 1) {
                System.out.println("1 carry operation.");
            } else {
                System.out.printf("%d carry operations.%n", step);
            }
        }
    }
}








Input: 
123 456  
555 555   
123 594 
0 0 
Output:
No carry operation. 
3 carry operations. 
1 carry operation.


