class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> cache = new HashMap<>();
        for (int num : nums) {
            if (cache.containsKey(num))
                return true;
            else
                cache.put(num, 1);
        }
        return false;
    }
}
