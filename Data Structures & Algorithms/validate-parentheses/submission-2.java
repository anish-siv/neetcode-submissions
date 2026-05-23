class Solution {
    public boolean isValid(String s) {
        ArrayDeque<Character> charStack = new ArrayDeque<>();

        char[] charArray = s.toCharArray();

        for(char i : charArray) {

            if(i == '(') {
                charStack.push(i);
            }
            if(i == '{') {
                charStack.push(i);
            }
            if(i == '[') {
                charStack.push(i);
            }
            if(i == ')') {
                if(charStack.isEmpty()) {
                    return false;
                }
                if(charStack.peek() == '(') {
                    charStack.pop();
                } else {
                    return false;
                }
            }
            if(i == '}') {
                if(charStack.isEmpty()) {
                    return false;
                }
                if(charStack.peek() == '{') {
                    charStack.pop();
                } else {
                    return false;
                }
            }
            if(i == ']') {
                if(charStack.isEmpty()) {
                    return false;
                }
                if(charStack.peek() == '[') {
                    charStack.pop();
                } else {
                    return false;
                }
            }
        }
        return charStack.isEmpty();
    }
}
