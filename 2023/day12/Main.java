package day12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    private static Map<Map<List<Character>, List<Integer>>, Long> prev_disp;

    // private static boolean checkDisposition(Character[] disp, Integer[] config) {
    //     int i = 0;
    //     int j = 0;
    //     int counter  = 0;

    //     if (Arrays.asList(disp).contains('?'))
    //         return false;

    //     while (i < disp.length && j < config.length) {
    //         counter = 0;
    //         while (disp[i] == '.') i++;
    //         while (disp[i] == '#') {
    //             counter++;
    //             i++;
    //         }
    //         if (counter != config[j])
    //             return false;
    //         j++;
    //     }
    //     if (j == config.length) {
    //         while (i < disp.length) {
    //             if (disp[i] == '#')
    //                 return false;
    //             i++;
    //         }
    //         return true;
    //     }
    //     return false;
    // }


    private static int min(int x, int y) {
        return x<y ? x:y;
    }

    // private static void printTotal(List<Character> disp, List<Integer> config, long total) {
    //         System.err.print(disp);
    //         System.err.print(" ");
    //         System.err.print(config);
    //         System.err.print(": ");
    //         System.err.println(total);
    // }

    private static long getTotal(List<Character> disp, List<Integer> config) {
        
        Map<List<Character>, List<Integer>> curr_disp = new HashMap<List<Character>, List<Integer>>();
        curr_disp.put(disp, config);
        if (prev_disp.containsKey(curr_disp))
            return prev_disp.get(curr_disp);
        curr_disp.clear();

        if (disp.size() == 0)
            return config.size() == 0 ? 1 : 0;
        if (config.size() == 0) 
            return disp.contains('#') ? 0 : 1;
        

        long total = 0;
        if (disp.get(0) == '.' || disp.get(0) == '?')  {
            total += getTotal(disp.subList(1, disp.size()), config);
        }

        if (disp.get(0) == '#' || disp.get(0) == '?') {
            if (config.get(0) <= disp.size() &&
                !disp.subList(0, config.get(0)).contains('.') &&
                (config.get(0) == disp.size() || disp.get(config.get(0)) != '#')) {
                
                total += getTotal(disp.subList(min(config.get(0)+1, disp.size()), disp.size()), config.subList(1, config.size()));     
            }
        }

        curr_disp.put(disp, config);
        prev_disp.put(curr_disp, total);
        return total;

    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        
        Row row;

        int total = 0;
        while ((row = reader.getRow(false)) != null) {
            List<Character> disp = row.getDisposition();
            List<Integer> config = row.getConfiguration();

            total += getTotal(disp, config);
        }

        System.out.println(total);

        



    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  
        
        Row row;
        

        long total = 0;
        while ((row = reader.getRow(true)) != null) {
            List<Character> disp = row.getDisposition();
            List<Integer> config = row.getConfiguration();

            total += getTotal(disp, config);
        }

        System.out.println(total);
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day12/day12_input.txt";

        prev_disp = new HashMap<Map<List<Character>, List<Integer>>, Long>();
    
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
