class Solution {
    String s1="";
    String s2="";
    int arr[][];
    public int longestCommonSubsequence(String text1, String text2) {
        s1=text1;
        s2=text2;
         arr=new int[text1.length()][text2.length()];
        for(int i=0;i<text1.length();i++){
            Arrays.fill(arr[i],-1);
        }
        return help(0,0);

    }
    public int help(int i,int j){
        if(i>=s1.length() || j>=s2.length()){
            return 0;
        }
        else if(arr[i][j]==-1){
            if(s1.charAt(i)==s2.charAt(j))
            return arr[i][j]=1+ help(i+1,j+1);
        }
        else if(arr[i][j]!=-1)return arr[i][j];
        return arr[i][j]=Math.max(help(i+1,j),help(i,j+1));
    }
}