print("Hellow world")

Practical 2
Minesweeper
 Have you ever played Minesweeper? It’s a cute little game which comes within a certain Operating System which name we can’t really remember. Well, the goal of the game is to find where are all the mines within a M × N field. To help you, the game shows a number in a square which tells you how many mines there are adjacent to that square. For instance, supose the following 4 × 4 field with 2 mines (which are represented by an ‘*’ character):
 *... 
....
 .*..
 ....
 If we would represent the same field placing the hint numbers described above, we would end up with: *100
 2210
 1*10 
1110
 As you may have already noticed, each square may have at most 8 adjacent squares. 
Input 
The input will consist of an arbitrary number of fields. The first line of each field contains two integers n and m (0 < n, m ≤ 100) which stands for the number of lines and columns of the field respectively. The next n lines contains exactly m characters and represent the field. Each safe square is represented by an ‘.’ character (without the quotes) and each mine square is represented by an ‘*’ character (also without the quotes). The first field line where n = m = 0 represents the end of input and should not be processed. Output
 For each field, you must print the following message in a line alone:
 Field #x:
 Where x stands for the number of the field (starting from 1). The next n lines should contain the field with the ‘.’ characters replaced by the number of adjacent mines to that square. There must be an empty line between field outputs. 
Sample Input
 4 4 
*...
 ....
 .*..
 .... **...
 .....
 .*... 
0 0
 Sample Output 
Field #1:
 *100 
2210 
1*10
 1110
 Field #2: 
**100
 33200 
1*100
Program





import java.util.*;
class Main {
public static void main(String... args) {
try {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt(), m = sc.nextInt(), i = 1;
String[] field = new String[n];
while (n != 0 && m != 0) {
if (i != 1) {
System.out.println("");
}
for (int j = 0; j < n; j++) {
field[j] = sc.next();
}
System.out.println(String.format("Field #%d:", i));
getAns(field, n, m);
n = sc.nextInt();
m = sc.nextInt();
i++;
field = new String[n];
}
} catch (Exception e) {
// Nothing to do here
} finally {
System.exit(0);
}
}
static void getAns(String[] field, int n, int m) {
int num;
for (int i = 0; i < n; i++) {
for (int j = 0; j < m; j++) {
if (field[i].charAt(j) == '*') {
System.out.print("*");
} else {
num = getNum(field, n, m, i, j);
System.out.print(num);
}
}
System.out.println("");
}
}
static int getNum(String[] field, int n, int m, int i, int j) {
int ans = 0;
for (int a = i-1; a <= i+1; a++) {
for (int b = j-1; b <= j+1; b++) {
if (a >= 0 && a < n && b >= 0 && b < m) {
ans = (field[a].charAt(b) == '*') ? ans+1 : ans;
}
}
}
return ans;
}
}




Input:
 4 4 
*...
 ....
 .*..
 .... **..
. .....
 .*... 
0 0
Output:
Field #1:
 *100 
2210 
1*10
 1110
 Field #2: 
**100
 33200 
1*100

