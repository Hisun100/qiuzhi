/*
*动态规划，设计一个数组存储状态，解决子问题间的重叠问题
*/
public class HouseRober {

    public int rob(int[] nums) {
    	if(nums.length ==0)
    		return 0;
    	//从最后一家开始搜索
    	int[] f =new int[nums.length+1]; //一维数组,存储状态
    	f[0]=0;
    	f[1]=nums[0];
        for(int i=2;i<=nums.length;++i)
    	     f[i] = Math.max(nums[i-1]+f[i-2],f[i-1]);
    	return f[nums.length];
    }
}
