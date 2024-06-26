print("Hellow World")



# Practical 3
# Jolly Jumpers 
# A sequence of n > 0 integers is called a jolly jumper if the absolute values of the difference between successive elements take on all the values 1 through n − 1. For instance, 
# 1 4 2 3
#  is a jolly jumper, because the absolutes differences are 3, 2, and 1 respectively. The definition implies that any sequence of a single integer is a jolly jumper. You are to write a program to determine whether or not each of a number of sequences is a jolly jumper.
#  Input
#  Each line of input contains an integer n ≤ 3000 followed by n integers representing the sequence. 
# Output 
# For each line of input, generate a line of output saying ‘Jolly’ or ‘Not jolly’. 
# Sample Input 
# 4 1 4 2 3
# 5 1 4 2 -1 6 
# Sample Output 
# Jolly Not jolly
# Program





# import java.io.BufferedReader;
# import java.io.IOException;
# import java.io.InputStreamReader;
# import java.util.BitSet;

# public class Main {
#     public static void main(String[] args) throws IOException {
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         String input;
#         // Read input from the console
#         while ((input = br.readLine()) != null && !input.trim().isEmpty()) {
#             String[] data = input.split("\\s+");

#             int numberOfInputs = Integer.parseInt(data[0]);
#             BitSet bitSet = new BitSet(numberOfInputs);
#             boolean isJolly = true;

#             for (int i = 1; i < data.length - 1; i++) {
#                 int diff = Math.abs(Integer.parseInt(data[i]) - Integer.parseInt(data[i + 1]));
#                 if (diff < 1 || diff >= numberOfInputs || bitSet.get(diff)) {
#                     isJolly = false;
#                     break;
#                 }
#                 bitSet.set(diff);
#             }
#             if (isJolly) {
#                 System.out.println("Jolly");
#             } else {
#                 System.out.println("Not jolly");
#             }
#         }
#     }
# }



# Input:
# 4 1 4 2 3
# 5 1 4 2 -1 6 
# Output:
# Jolly 
# Not jolly

