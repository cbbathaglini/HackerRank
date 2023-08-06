
/* https://www.hackerrank.com/challenges/java-output-formatting/submissions/code/338495991 */
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String s1 = sc.next();
            int x = sc.nextInt();

            int lenword = s1.length();
            int lennum = Integer.toString(x).length();
            int sobraletra = 15 - lenword;
            int sobranum = 3 - lennum;
            System.out.printf(s1);
            for (int e = 0; e < sobraletra; e++) {
                System.out.printf(" ");
            }

            if (sobranum > 0) {
                for (int e = 0; e < sobranum; e++) {
                    System.out.printf("0");
                }
            }
            System.out.printf(Integer.toString(x));

            System.out.printf("\n");
            // System.out.printf("%"+sobraletra+"s%"+lenword+"s%"+lennum+"d%"+sobranum+"s\n","
            // ",s1,x, "0");
        }
        System.out.println("================================");

    }
}
