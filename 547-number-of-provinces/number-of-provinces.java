class Solution {
    boolean visited[];
    public int findCircleNum(int[][] a) {
        int c=0;
        visited=new boolean[a.length];
        for(int i=0;i<a.length;i++){
            if(!visited[i]){
                help(i,a);
                c++;
            }
        }
        return c;
    }
    public void help(int i,int a[][]){
        visited[i]=true;
        for(int k=0;k<a[0].length;k++){
            if(!visited[k]){
                if(a[i][k]==1){
                    help(k,a);
                }
            }
        }
    }
}