class Solution {
    String s1="";
    String s2="";
    int arr[][];
    public int longestPalindromeSubseq(String s) {
        s1=s;
        s2=new StringBuilder(s).reverse().toString();
        arr=new int[s1.length()][s2.length()];
        for(int i=0;i<s1.length();i++){
            Arrays.fill(arr[i],-1);
        }
        return help(0,0);
    }
    public int help(int i,int j){
        if(i>=s1.length() ||j>=s2.length()){
            return 0;
        }
        if(arr[i][j]!=-1){
            return arr[i][j];
        }
            if(s1.charAt(i)==s2.charAt(j)){
                return arr[i][j]=1+ help(i+1,j+1);
            }
        
        return arr[i][j]=Math.max(help(i+1,j),help(i,j+1));
        
    }
}