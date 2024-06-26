print("Heloow world")








Practical 5
Where’s Waldorf? 
Given a m by n grid of letters, (1 ≤ m, n ≤ 50), and a list of words, find the location in the grid at which the word can be found. 
A word matches a straight, uninterrupted line of letters in the grid. A word can match the letters in the grid regardless of case (i.e. upper- and lower-case letters are to be treated as the same). The matching can be done in any of the eight directions either horizontally, vertically or diagonally through the grid. 
Input 
The input begins with a single positive integer on a line by itself indicating the number of the cases following, each of them as described below. This line is followed by a blank line, and there is also a blank line between two consecutive inputs. The input begins with a pair of integers, m followed by n, 1 ≤ m, n ≤ 50 in decimal notation on a single line. The next m lines contain n letters each; this is the grid of letters in which the words of the list must be found. The letters in the grid may be in upper or lower case. Following the grid of letters, another integer k appears on a line by itself (1 ≤ k ≤ 20). The next k lines of input contain the list of words to search for, one word per line. These words may contain upper and lower case letters only (no spaces, hyphens or other non-alphabetic characters). 
Output
 For each test case, the output must follow the description below. The outputs of two consecutive cases will be separated by a blank line. For each word in the word list, a pair of integers representing the location of the corresponding word in the grid must be output. The integers must be separated by a single space. The first integer is the line in the grid where the first letter of the given word can be found (1 represents the topmost line in the grid, and m represents the bottommost line). The second integer is the column in the grid where the first letter of the given word can be found (1 represents the leftmost column in the grid, and n represents the rightmost column in the grid). If a word can be found more than once in the grid, then the location which is output should correspond to the uppermost occurence of the word (i.e. the occurence which places the first letter of the word closest to the top of the grid). If two or more words are uppermost, the output should correspond to the leftmost of these occurences. All words can be found at least once in the grid.
 Sample Input 
1 
8 11 
abcDEFGhigg
hEbkWalDork 
FtyAwaldORm 
FtsimrLqsrc 
byoArBeDeyv 
Klcbqwikomk 
strEBGadhrb 
yUiqlxcnBjf 
4 
Waldorf 
Bambi 
Betty 
Dagbert 
Sample Output 
2 5 
2 3 
1 2 
7 8
Program








import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static String word;
    static char[][] grid;
    static boolean find(int index, int i, int j) {
        if (index >= word.length()) return true;
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length) return false;
        if (grid[i][j] != word.charAt(index)) return false;
        int[][] directions = {
                {0,1},
                {1,0},
                {-1,0},
                {0,-1},
                {1,1},
                {1,-1},
                {-1,1},
                {-1,-1}
        };
        boolean found = false;
        for (int[] direction: directions) {
             found = found || find(index + 1, i + direction[0], j + direction[1], direction);
        }
        return found;
    }
    static boolean find(int index, int i, int j, int[] direction) {
        if (index >= word.length()) return true;
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[i].length) return false;
        if (grid[i][j] != word.charAt(index)) return false;
        return find(index + 1, i + direction[0], j + direction[1], direction);
    }
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int cases = Integer.parseInt(in.readLine());
        for (int c = 0; c < cases; c++) {
            in.readLine();
            String[] temp = in.readLine().split("\\s+");
            int m = Integer.parseInt(temp[0]);
            int n = Integer.parseInt(temp[1]);
            grid = new char[m][n];
            for (int i = 0; i < m; i++) {
                String s = in.readLine();
                s = s.toLowerCase();
                for (int j = 0; j < n; j++) {
                    grid[i][j] = s.charAt(j);
                }  }
//            for (char[] t: grid) System.out.println(Arrays.toString(t));
            int Q = Integer.parseInt(in.readLine());
            for (int q = 0; q < Q; q++) {
                boolean found = false;
                word = in.readLine();
                word = word.toLowerCase();
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (find( 0, i, j)) {
                            System.out.printf("%d %d\n", i + 1, j + 1);
                            found = true;
                            break;
                        }     }
                    if (found) break;
                }   }
            if (c < cases - 1) System.out.println();
        }  }  }







Input:                                                                                                                
1 
8 11 
abcDEFGhigg
hEbkWalDork 
FtyAwaldORm 
FtsimrLqsrc 
byoArBeDeyv 
Klcbqwikomk 
strEBGadhrb 
yUiqlxcnBjf 
4 
Waldorf 
Bambi 
Betty 
Dagbert 
Output:
2 5 
2 3 
1 2 
7 8



