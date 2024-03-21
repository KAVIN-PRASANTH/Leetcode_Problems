class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int arr[][]=new int[text1.length()+1][text2.length()+1];
        for(int i=0;i<=text1.length();i++){
            for(int j=0;j<=text2.length();j++){
                if(i==0 || j==0){
                    arr[i][j]=0;
                }
                else if(text1.charAt(i-1)==text2.charAt(j-1)){
                     arr[i][j]=arr[i-1][j-1]+1;
                    
                }
                else{
                   arr[i][j]=Math.max(arr[i-1][j],arr[i][j-1]);
                }
            }
        }
        return arr[text1.length()][text2.length()];
    }
}