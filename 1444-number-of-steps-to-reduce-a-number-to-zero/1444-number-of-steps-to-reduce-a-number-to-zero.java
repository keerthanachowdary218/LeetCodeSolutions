class Solution {
    //int i=1;
    public int numberOfSteps(int num) {
        //System.out.println(demo());
        return help(num);
    }
    int help(int num){
        if(num==0){
            //System.out.println(i);
            return 0;
        }
        if(num%2==0){
            return 1+help(num/2);
        }
        else{
            return 1+help(num-1);
        }
    }
    /*
    ArrayList demo(){
        return new ArrayList<>();
    }
    */
}