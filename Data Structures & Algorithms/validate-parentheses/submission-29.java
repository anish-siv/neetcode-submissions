class Solution {
    public boolean isValid(String s) {
        // Create a HashMap to store KV pairs (Character)
        // Create an empty Stack
        
        // For each char in the String
            // If the stack is empty or the popped char from stack != char value
                // Return false
            // else
                // Push open char to Stack
        // Return stack if not empty

        HashMap<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put('}', '{');
        pairs.put(']', '[');
        
        Deque<Character> stack = new ArrayDeque<>();
        
        for(int i = 0; i < s.length(); i++) {
            if(pairs.containsKey(s.charAt(i))) {
                if(stack.isEmpty() || (stack.pop() != pairs.get(s.charAt(i)))) {
                    return false;
                } 
            }
            else
                stack.push(s.charAt(i)); 
        }
        return stack.isEmpty();
    }
}
