class Solution {
    public String stringShift(String s, int[][] shift) {
        String s_ = s;
        String new_word = "";
        for (int i = 0; i < shift.length; i++) {
            int[] matrix = shift[i];
            int direction = matrix[0];
            int amount = matrix[1];
            
            if (direction == 0) {
                amount = amount % s_.length();
                new_word = s_.substring(amount, s_.length()) + s_.substring(0, amount);
            } else if (direction == 1) {
                amount = amount % s_.length();
                String c = s_.substring(s_.length()-amount);
                new_word = c + s_.substring(0, amount);
            }
            s_ = new_word;
        }

        return new_word;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        // int[][] shift = new int[][]{ {1,4} };
        int[][] shift = new int[][]{ {1,2}  };

        String res = s.stringShift("bca", shift);
        System.out.println(res);
    }
}

