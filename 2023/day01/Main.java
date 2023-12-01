package day01;
import java.util.*;

public class Main {

    private static final Map<String, Integer> numberDict = new HashMap<String, Integer>() {{
        put("zero", 0);
        put("one", 1);
        put("two", 2);
        put("three", 3);
        put("four", 4);
        put("five", 5);
        put("six", 6);
        put("seven", 7);
        put("eight", 8);
        put("nine", 9);
    }};

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        int sum = 0;
        for (String s : reader.GetInfo()) {
            int first = -1;
            int last = -1;
            int i = 0;
            while (first == -1 || last == -1) {
            
                if (first == -1 && Character.isDigit(s.charAt(i)))
                    first = Character.getNumericValue(s.charAt(i));
                if (last == -1 && Character.isDigit(s.charAt(s.length() - 1 - i)))
                    last = Character.getNumericValue(s.charAt(s.length() - 1 -  i));
                i++;
            }
            sum += first*10 + last;
        }
        System.out.println(sum);
    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        int sum = 0;
        for (String s : reader.GetInfo()) {
            int first = -1;
            int last = -1;
            int i = 0;
            while (first == -1 || last == -1) {
                if (first == -1) {
                    if (Character.isDigit(s.charAt(i))) {
                        first = Character.getNumericValue(s.charAt(i));
                    }
                    for (String num : numberDict.keySet()) {
                        if (s.substring(i).indexOf(num) == 0)
                            first = numberDict.get(num);
                    }
                }
                if (last == -1) {
                    if (Character.isDigit(s.charAt(s.length() - 1 - i))) {
                        last = Character.getNumericValue(s.charAt(s.length() - 1 - i));
                    }
                    for (String num : numberDict.keySet()) {
                        if (s.substring(s.length() - 1 - i).indexOf(num) == 0)
                            last = numberDict.get(num);
                    }
                }
                i++;
            }
            sum += first*10 + last;
        }
        System.out.println(sum);
    }
    public static void main(String[] args) {

        String file_name = "day01/day01_input.txt";

        try {
            part1(file_name);
        } catch (Exception e) {
            System.err.println("Part 1 Failed " + e);
        }
        try {
            part2(file_name);
        } catch (Exception e) {
            System.err.println("Part 2 Failed " + e);
        }

    }
}
