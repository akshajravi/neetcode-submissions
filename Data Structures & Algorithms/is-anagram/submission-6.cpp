class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length() != t.length()) return false;

        unordered_map<char,int> anagram;

        for(auto c : s){
            anagram[c]++;
        }

        for(auto c : t){
            anagram[c]--;
            if(anagram[c] < 0){
                return false;
            }
        }

        return true;
    }
};
