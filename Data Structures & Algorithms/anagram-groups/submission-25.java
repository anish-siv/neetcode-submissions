class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Create a new HashMap groups (Key = Alpha sorted strings : Value = List of strings when alpha sorted match key)
        // For each string in strs
            // Create a new char array that creates a char array from a String
            // Sort the string into an alphabetical form (e.g. "eat" -> "aet")
            // Place the sorted string into a String variable for keys
            // If the key is in not in groups
                // Put the key in groups with a new empty list
            // Add the word to the list for that key
        // Return a new ArrayList of groups' values

        HashMap<String, List<String>> groups = new HashMap<>();

        for( String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            if(!groups.containsKey(key)) {
                groups.put(key, new ArrayList<>());
            }
            groups.get(key).add(str);
        }
        return new ArrayList<>(groups.values());
    }
}
