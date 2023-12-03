package day03;
import java.util.*;

public class Main {
    
    private static List<Coords> dirs;

    private static int getNum(List<Character> row, int pos) {
        int num = 0;

        while (pos > 0 && Character.isDigit(row.get(pos-1))) {
            pos--;
        }
        while (pos < row.size() && Character.isDigit(row.get(pos))) {
            num *= 10;
            num += Character.getNumericValue(row.get(pos));
            row.set(pos, '.');
            pos++;
        }

        return num;
    }

    private static List<Integer> getNums(List<List<Character>> table, Coords curr) {
        List<Integer> nums = new ArrayList<>();
        Coords pos;
        
        for (Coords dir: dirs) {
            
            pos = curr.sum(dir);
            if (Character.isDigit(table.get(pos.getX()).get(pos.getY()))) {
                nums.add(getNum(table.get(pos.getX()), pos.getY()));
            }
        } 

        return nums;
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<List<Character>> table = reader.GetTable();
        
        int sum = 0;
        for (List<Character> row : table) {
            for (Character c : row) {
                if (c != '.' && c != '\n' && !Character.isDigit(c)) {
                    Coords pos = new Coords(table.indexOf(row), row.indexOf(c));
                    for (int n : getNums(table, pos)) {
                        sum += n;
                    }
                    row.set(pos.getY(), '.');   
                }
            }
        }
        System.out.println(sum);


    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<List<Character>> table = reader.GetTable();
        List<Integer> nums;
        
        int sum = 0;
        for (List<Character> row : table) {
            for (Character c : row) {
                if (c == '*') {
                    Coords pos = new Coords(table.indexOf(row), row.indexOf(c));
                    nums = getNums(table, pos);
                    if (nums.size() == 2) {
                        sum += nums.get(0) * nums.get(1);
                    }
                    row.set(pos.getY(), '.');   
                }
            }
        }
        System.out.println(sum);

    }

    public static void main(String[] args) throws Exception {
        
        dirs = new ArrayList<Coords>();
        for (int i = -1; i <= 1; i++) {
            for (int j = -1; j <= 1; j++) {
                dirs.add(new Coords(i, j));
            }
        }

        String file_name = "day03/day03_input.txt";

        part2(file_name);

        // try {
        //     part1(file_name);
        // } catch (Exception e) {
        //     System.err.println("Part 1 Failed " + e);
        // }
        // try {
        //     part2(file_name);
        // } catch (Exception e) {
        //     System.err.println("Part 2 Failed " + e);
        // }

    }   
}
