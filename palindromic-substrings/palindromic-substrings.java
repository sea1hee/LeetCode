class Solution {
    public int countSubstrings(String s) {
        if ( s== null || s.equals("")){
            return 0;
        }
        
        char[] charArr = s.toCharArray();
        int cnt = 0;
        
        for (int i = 0; i< charArr.length; i++){
            String pStr = Character.toString(charArr[i]);
            cnt++;
            for ( int j = i+1; j< charArr.length; j++){
                pStr = pStr.concat(Character.toString(charArr[j]));
                if(pStr.equals(new StringBuffer(pStr).reverse().toString())){
                    cnt++;
                }
            }
        }
        
        return cnt;
    }
}