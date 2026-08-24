// Last updated: 8/24/2026, 3:53:28 PM
1class Solution {
2    public int lengthOfLastWord(String s)
3     {
4        s = s.trim();
5        int last_count =0;
6       
7        for(int i=s.length()-1;i>=0;i--){
8        if(s.charAt(i)==' '){
9            break;
10        }
11            last_count++;
12        
13        }
14    
15    return last_count;
16     }
17}