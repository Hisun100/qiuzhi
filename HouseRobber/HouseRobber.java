/*
 * 偷盗者问题：不可偷盗相邻房舍，求偷盗财物的最大价值
 * 
 */
public class HouseRober {

    public int search(int idx, int[] nums) {
    	//计算盗取财物的最大值
    	/*
    	 * 情况一：偷取当前房舍 nums[idx]+search(idx-2, nums)
    	 * 情况二：偷取当前房舍的隔壁家  search(idx-1, nums)
    	 */
    	if(idx <0) return 0; //边界条件：无房舍可偷盗
    	return Math.max(nums[idx]+search(idx-2, nums),search(idx-1, nums));
    }
    public int rob(int[] nums) {
    	//从最后一家开始搜索
    	return search(nums.length-1, nums);
    }
}
