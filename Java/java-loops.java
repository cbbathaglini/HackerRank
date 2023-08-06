/* https://www.hackerrank.com/challenges/java-loops/submissions/code/338917876 */
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int calculo = 0 ;
            
            for(int j=0; j<n; j++){
                
                calculo =  a + Solution.recursao(j,b,0,0);  
                System.out.print(calculo+ " ");
            }
            System.out.println();
        }
        in.close();
    
    }
    public static int recursao( int j, int b, int calculo,int contador){
       if(contador<=j){
         calculo += Math.pow(2,contador) * b;
         //System.out.println(calculo);
         contador++;
       }else{
           //System.out.println("----");
           return calculo;
       }
       return recursao(j, b,calculo, contador);
    }
}