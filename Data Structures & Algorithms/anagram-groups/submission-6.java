class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> groupedStrings = new HashMap<>();

        for(String str : strs) {
            char[] charArray = str.toCharArray();
            Arrays.sort(charArray);
            String sortedString = new String(charArray);

            List<String> list = groupedStrings.getOrDefault(sortedString, new ArrayList<>());
            list.add(str);
            groupedStrings.put(sortedString, list);
        }
        return new ArrayList<>(groupedStrings.values());
    }
}
