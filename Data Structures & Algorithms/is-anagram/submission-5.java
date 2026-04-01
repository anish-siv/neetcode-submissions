class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) {
            return false;
        }

        int[] char_count = new int[26];

        for(int i = 0; i < s.length(); i++) {
            char s_curr = s.charAt(i);
            char_count[s_curr - 'a']++;
        }

        for(int j = 0; j < t.length(); j++) {
            char t_curr = t.charAt(j);
            char_count[t_curr - 'a']--;
        }
        
        for(int k = 0; k < char_count.length; k++) {
            if(char_count[k] != 0) {
                return false;
            }
        }
        return true;
    }
}
