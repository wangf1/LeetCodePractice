package leetcodepractice;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {

    public static final int SUDOKU_LENGTH = 9;

    public boolean isValidSudoku(char[][] board) {
        boolean valid = validateRows(board);
        if (!valid) {
            return valid;
        }
        valid = validateColumns(board);
        if (!valid) {
            return valid;
        }
        return validateSubBoxes(board);
    }


    private boolean validateRows(char[][] board) {
        for (char[] row : board) {
            if (lineInvalid(row)) {
                System.out.printf("Row invalid: %s%n", Arrays.toString(row));
                return false;
            }
        }
        return true;
    }

    private boolean lineInvalid(char[] line) {
        Map<Character, Integer> count = new HashMap<>();
        for (char c : line) {
            if (c == '.') {
                continue;
            }
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        return count.values().stream().anyMatch(v -> v >= 2);
    }

    private boolean validateColumns(char[][] board) {
        for (int c = 0; c < SUDOKU_LENGTH; c++) {
            char[] column = new char[SUDOKU_LENGTH];
            for (int r = 0; r < SUDOKU_LENGTH; r++) {
                column[r] = board[r][c];
            }
            if (lineInvalid(column)) {
                System.out.printf("Column invalid: %s%n", Arrays.toString(column));
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
                int rStart = i * 3;
                int cStart = j * 3;
                for (int r = rStart; r < rStart + 3; r++) {
                    for (int c = cStart; c < cStart + 3; c++) {
                        cells[cellIndex++] = board[r][c];
                    }
                }
                if (lineInvalid(cells)) {
                    System.out.printf("Sub-box invalid: %s%n", Arrays.toString(cells));
                    return false;
                }
            }
        }
        return true;
    }
}