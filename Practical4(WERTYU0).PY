print("Hellow World")


Practical 4
WERTYU 
A common typing error is to place the hands on the keyboard one row to the right of the correct position. So ‘Q’ is typed as ‘W’ and ‘J’ is typed as ‘K’ and so on. You are to decode a message typed in this manner.
 Input 
Input consists of several lines of text. Each line may contain digits, spaces, upper case letters (except Q, A, Z), or punctuation shown above [except back-quote (`)]. Keys labelled with words [Tab, BackSp, Control, etc.] are not represented in the input. 
Output
 You are to replace each letter or punction symbol by the one immediately to its left on the ‘QWERTY’ keyboard shown above. Spaces in the input should be echoed in the output. 
Sample Input 
O S, GOMR YPFSU/ 
Sample Output
 I AM FINE TODAY.
Program






import java.util.HashMap;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        HashMap<Character, Character> k = new HashMap<>();
        k.put('2', '1'); k.put('3', '2');
        k.put('4', '3'); k.put('5', '4');
        k.put('6', '5');
        k.put('7', '6');
        k.put('8', '7');
        k.put('9', '8');
        k.put('0', '9');
        k.put('-', '0');
        k.put('=', '-');
        k.put('W', 'Q');
        k.put('E', 'W');
        k.put('R', 'E');
        k.put('T', 'R');
        k.put('Y', 'T');
        k.put('U', 'Y');
        k.put('I', 'U');
        k.put('O', 'I');
        k.put('P', 'O');
        k.put('[', 'P');
        k.put(']', '[');
        k.put('\\', ']');
        k.put('S', 'A');
        k.put('D', 'S');
        k.put('F', 'D');
        k.put('G', 'F');
        k.put('H', 'G');
        k.put('J', 'H');
        k.put('K', 'J');
        k.put('L', 'K');
        k.put(';', 'L');
        k.put('\'', ';');
        k.put('X', 'Z');
        k.put('C', 'X');
        k.put('V', 'C');
        k.put('B', 'V');
        k.put('N', 'B');
        k.put('M', 'N');
        k.put(',', 'M');
        k.put('.', ',');
        k.put('/', '.');
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                char[] n = scanner.nextLine().toCharArray();
                for (char i : n) {
                    if (i != ' ') {
                        System.out.print(k.get(i));
                    } else {
                        System.out.print(" ");
                    }
                }
                System.out.println();
            } catch (Exception e) {
                break;
            }
        }
    }
}





Input:
O S, GOMR YPFSU/ 
Output:
 I AM FINE TODAY.


