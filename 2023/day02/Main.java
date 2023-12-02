package day02;
import java.util.*;

public class Main {


    private static final int NUM_RED = 12;
    private static final int NUM_GREEN = 13;
    private static final int NUM_BLUE = 14;

    private static int mapper(Color c) {
        if (c == Color.RED)
            return NUM_RED;
        if (c == Color.GREEN)
            return NUM_GREEN;
        if (c == Color.BLUE)
            return NUM_BLUE;
        return -1;
    }


    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        int i = 1;
        int sum = 0;
        List<Map<Color, Integer>> game;
        boolean possible;
        while ((game = reader.GetLine()) != null) {
            possible = true;
            for (Map<Color, Integer> round : game) {
                for (Color c : round.keySet()) {
                    if (mapper(c) < round.get(c))
                        possible = false;

                        break;
                }
                if (!possible)
                    break;

            }
            if (possible) {
                sum += i;
            }
            i++;
            
        }
        System.out.println(sum);
    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        Map<Color, Integer> game;

        int sum = 0;
        int power;
        while ((game = reader.GetMin()) != null) {
            power = 1;
            for (Color c: game.keySet()) {
                power *= game.get(c);
            }
            sum += power;
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {

        String file_name = "day02/day02_input.txt";

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
