class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groupedStrings = new HashMap<>();

        for(String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);

            if(groupedStrings.containsKey(sortedString)) {
                // key exists — add str to the existing list
                List<String> list = groupedStrings.get(sortedString);
                list.add(str);
            } else {
                // key doesn't exist — create a new list and put it in the map
                List<String> list = new ArrayList<>();
                list.add(str);
                groupedStrings.put(sortedString, list);
            }
        }
        return new ArrayList<>(groupedStrings.values());
    }
}
