import java.io.*;
import java.util.*;

public class Solution {

    static int H;
    static int B;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        B = in.nextInt();
        H = in.nextInt();

        if (B <= 0 || H <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
            return;
        }

        System.out.println(B * H);
    }
}