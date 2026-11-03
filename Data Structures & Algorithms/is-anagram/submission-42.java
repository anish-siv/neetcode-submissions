class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        int[] char_counts = new int[26];

        for(int i = 0; i < s.length(); i++) {
            char_counts[sArray[i] - 'a']++;
            char_counts[tArray[i] - 'a']--;
        }

        for(int count : char_counts) {
            if(count != 0) {
                return false;
            }
        }
        return true;
    }
}
