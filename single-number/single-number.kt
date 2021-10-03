class Solution {
    fun singleNumber(nums: IntArray): Int {
        
        val sortedNums = nums.sorted()
        var returnNum = sortedNums[sortedNums.size-1]
        
        for (i :Int in 0 until sortedNums.size-1 step 2){
            if (sortedNums[i] != sortedNums[i+1]){
                returnNum = sortedNums[i]
                break
            }
        }
        
        return returnNum
    }
}