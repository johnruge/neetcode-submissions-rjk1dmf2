class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs); 
        int strsLen = strs.length;
        int shortest = strs[0].length();
        for (int i = 0; i < shortest; i ++) {
            if (strs[0].charAt(i) != strs[strsLen - 1].charAt(i)) {
                return strs[0].substring(0, i);
            } 
        }
        return strs[0];
    }
}