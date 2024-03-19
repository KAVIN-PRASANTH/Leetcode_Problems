class Solution {
    public String largestNumber(int[] nums) {
        Comparator<String> cmp=new Comparator<>(){
            public int compare(String a,String b){
               return (b+a).compareTo(a+b);
            }
        };
        String s[]=new String[nums.length];
        for(int i=0;i<nums.length;i++){
            s[i]=nums[i]+"";
        }
        Arrays.sort(s,cmp);
        String s1="";
        for(int i=0;i<nums.length;i++){
            s1+=s[i];
        }
        if(s1.charAt(0)=='0')return 0+"";
        return s1;
    }
}