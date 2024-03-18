class Solution {
    public void nextPermutation(int[] nums) {
        int in=-1;
        for(int i=nums.length-2;i>=0;i--)
        {
            if(nums[i]<nums[i+1]){
                in=i;
                break;
            }
        }
        if(in==-1){
            for(int i=0;i<nums.length/2;i++){
                int temp=nums[i];
                nums[i]=nums[nums.length-1-i];
                nums[nums.length-1-i]=temp;

            }
           return ;
        }
        int b=0;
        for(int i=nums.length-1;i>in;i--){
            if(nums[i]>nums[in]){
              b=i;
              break;
            }
              
        }
        int temp=nums[in];
        nums[in]=nums[b];
        nums[b]=temp;
      
        int kk=0;
        for(int i=in+1;i<=((nums.length-(in+1))/2)+in;i++){
           
                int q=nums[i];
                nums[i]=nums[nums.length-1-kk];
             
                nums[nums.length-1-kk]=q;
                   kk++;

            }
        
        

    }
}