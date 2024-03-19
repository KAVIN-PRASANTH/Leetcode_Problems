class Solution {
    public int findMinArrowShots(int[][] arr) {
        Arrays.sort(arr,(a,b)->Integer.compare(a[1],b[1]));
        int a=1;
        int pre=arr[0][1];
        for(int i=1;i<arr.length;i++){
            if(arr[i][0]>pre){
                pre=arr[i][1];
                a++;
            }
        }

        return a;
    }
}