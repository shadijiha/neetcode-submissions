class Solution {
    public int getSum(int a, int b) {
        //   0101
        //   0100
        //   
        int withoutCarry = a ^ b;
        int carry = a & b;

        return carry == 0 ? withoutCarry : getSum(withoutCarry, carry << 1);  
    }
}
