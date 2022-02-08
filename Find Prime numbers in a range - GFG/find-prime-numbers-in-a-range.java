// { Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            int M = Integer.parseInt(S[0]);
            int N = Integer.parseInt(S[1]);
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.primeRange(M, N);
            for (int i : ans) System.out.print(i + " ");
            System.out.println();
        }
    }
}// } Driver Code Ends


// User function Template for Java

class Solution {
   ArrayList<Integer> primeRange(int M, int N) {
       // code here
       ArrayList<Integer> al = new ArrayList<>();
       while(M<=N){
           if(isPrime(M)) al.add(M);
           M++;
       }
       
       return al;
   }
   
   boolean isPrime(int n){
       if(n<=1) return false;
       else if(n==2) return true;
       else if(n%2==0) return false;
       
       for(int i=3;i*i<=n;i = i+2){
           if(n%i==0) return false;
       }
       
       return true;
   }
}