package day08;

import java.util.List;

public class Main {


    public static long MCD(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }


    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Integer> instructions = reader.getInstructions();
        Network net = reader.getNetwork();

        int counter = 0;
        while (!net.getCurr().equals("ZZZ")) {
            for (int i: instructions) {
                net.followInstruction(i);
                counter++;
                if (net.getCurr().equals("ZZZ"))
                    break;
            }
        }
        System.out.println(counter);
    
        
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Integer> instructions = reader.getInstructions();
        Network net = reader.getNetwork();
        

        long total = 1;
        for (String s: net.getNodes()) {
            if (!s.endsWith("A"))
                continue;
            long counter = 0;
            net.setStartPosition(s);
            while (!net.getCurr().endsWith("Z")) {
                for (int i: instructions) {
                    net.followInstruction(i);
                    counter++;
                    if (net.getCurr().endsWith("Z"))
                        break;
                }
            }
            total = total*counter / MCD(total, counter);
        }
        System.out.println(total);

    }

    public static void main(String[] args) throws Exception {

        String file_name = "day08/day08_input.txt";

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