class Solution {
    public int numRescueBoats(int[] a, int lim) {
        Arrays.sort(a);
        int l=0,r=a.length-1,sum=0,b=0,flag=0;
        while(l<=r){
            if(flag!=2 &&sum+a[r]<=lim){
                sum+=a[r--];
                flag++;
            }
            else if(flag!=2 &&sum+a[l]<=lim){
                sum+=a[l++];
                flag++;
            }
            else{
                flag=sum=0;
                b++;
            }
        }
        if(sum!=0)b++;
        return b;
    }
}