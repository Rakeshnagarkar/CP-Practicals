print("Hello World")










Practical 6
Vito’s family 
The world-known gangster Vito Deadstone is moving to New York. He has a very big family there, all of them living in Lamafia Avenue. Since he will visit all his relatives very often, he is trying to find a house close to them. Vito wants to minimize the total distance to all of them and has blackmailed you to write a program that solves his problem.
 Input 
The input consists of several test cases. The first line contains the number of test cases. For each test case you will be given the integer number of relatives r (0 < r < 500) and the street numbers (also integers) s1, s2, . . . , si , . . . , sr where they live (0 < si < 30000 ). Note that several relatives could live in the same street number.
Output 
For each test case your program must write the minimal sum of distances from the optimal Vito’s house to each one of his relatives. The distance between two street numbers si and sj is dij = |si − sj |. 
Sample Input
 2
 2 2 4
 3 2 4 6
 Sample Output
 2 4

Program











 import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        while (test-- > 0) {
            int n = scanner.nextInt();
            int[] elements = new int[n];

            for (int index = 0; index < n; index++)
                elements[index] = scanner.nextInt();
            for (int row = 0; row < n - 1; row++) {
                for (int column = 0; column < n - row - 1; column++) {
                    if (elements[column] > elements[column + 1]) {
                        int temp = elements[column];
                        elements[column] = elements[column + 1];
                        elements[column + 1] = temp;
                    }
                }
            }
            int distance = 0;
            for (int index = 0; index < n; index++) {
                distance += Math.abs(elements[n / 2] - elements[index]);
            }
            System.out.println(distance);
        }
    }
}










Input:
 2
 2 2 4
 3 2 4 6
Output:
2 4
