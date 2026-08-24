// Last updated: 8/24/2026, 4:20:34 PM
1class Solution {
2    public boolean isPalindrome(String s) {
3        String check = "";
4        for(int i = 0; i<s.length();i++){
5            if(Character.isLetterOrDigit(s.charAt(i))){
6                check += s.charAt(i);
7            }
8        }
9        check = check.toLowerCase();
10        int x = check.length()-1;
11        for(int i = 0; i<x; i++){
12            if(check.charAt(i)!=check.charAt(x)){
13                return false;
14            }
15            x--;
16        }
17        return true;
18    }
19}