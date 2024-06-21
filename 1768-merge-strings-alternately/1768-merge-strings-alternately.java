class Solution {
    public String mergeAlternately(String word1, String word2) {
        int count = 0;
        String merged = "";
        while (count < word1.length() || count < word2.length()) {
            if (count < word1.length()) {
                merged = merged + word1.charAt(count);
            } 
            if (count < word2.length()) {
                merged = merged + word2.charAt(count);
            }
            count ++;
        }
        return merged;
    }
}