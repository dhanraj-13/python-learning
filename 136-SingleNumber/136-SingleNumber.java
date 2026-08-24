// Last updated: 8/24/2026, 4:19:30 PM
1class Solution {
2    public int singleNumber(int[] nums) {
3        int xorr = 0;
4
5        for (int num : nums) {
6            xorr ^= num;
7        }
8
9        return xorr;
10    }
11}