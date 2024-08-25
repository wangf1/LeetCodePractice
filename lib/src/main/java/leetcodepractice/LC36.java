package leetcodepractice;

import java.util.HashSet;
import java.util.Set;

class Solution {

    public static final int SUDOKU_LENGTH = 9;

    public boolean isValidSudoku(char[][] board) {
        return validateRows(board) && validateColumns(board) && validateSubBoxes(board);
    }

    private boolean validateRows(char[][] board) {
        for (char[] row : board) {
            if (containsDuplicate(row)) {
                System.out.printf("Row invalid: %s%n", new String(row));
                return false;
            }
        }
        return true;
    }

    private boolean validateColumns(char[][] board) {
        for (int c = 0; c < SUDOKU_LENGTH; c++) {
            char[] column = new char[SUDOKU_LENGTH];
            for (int r = 0; r < SUDOKU_LENGTH; r++) {
                column[r] = board[r][c];
            }
            if (containsDuplicate(column)) {
                System.out.printf("Column invalid: %s%n", new String(column));
                return false;
            }
        }
        return true;
    }

    private boolean validateSubBoxes(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                char[] cells = new char[SUDOKU_LENGTH];
                int cellIndex = 0;
                for (int r = i * 3; r < i * 3 + 3; r++) {
                    for (int c = j * 3; c < j * 3 + 3; c++) {
                        cells[cellIndex++] = board[r][c];
                    }
                }
                if (containsDuplicate(cells)) {
                    System.out.printf("Sub-box invalid: %s%n", new String(cells));
                    return false;
                }
            }
        }
        return true;
    }

    private boolean containsDuplicate(char[] line) {
        Set<Character> seen = new HashSet<>();
        for (char c : line) {
            if (c != '.' && !seen.add(c)) {
                return true;
            }
        }
        return false;
    }
}
