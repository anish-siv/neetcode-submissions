class Solution {
    public boolean isAnagram(String s, String t) {
        // Create an empty int array counts of size 26

        // Easy check here
        // If the lengths of s and t are not equal
            // Return false

        // For each character in s
            // Increment the # of times a character appears
            // This involves subtracting 'a' from each char to get an index from 0 - 25 and incrementing counts at that index
        
        // For each character in t
            // Decrement the # of times a character appears
            // This involves subtracting 'a' from each char to get an index from 0 - 25 and decrementing counts at that index
        
        // Use an enhanced for loop that will count what remains in counts
            // If count != 0
                // Return false
        // Return true

        int[] counts = new int[26];

        if(s.length() != t.length()) {
            return false;
        }

        for(char c : s.toCharArray()) {
            counts[c - 'a']++;
        }

        for(char c : t.toCharArray()) {
            counts[c - 'a']--;
        }

        for(int count : counts) {
            if(count != 0) {
                return false;
            }
        }
        return true;
    }
}
