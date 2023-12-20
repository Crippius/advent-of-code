package day15;

import java.util.*;

public class Main {

    private static int hash(String code) {
        int current_value = 0;
        for (char c: code.toCharArray()) {
            current_value += (int) c;
            current_value *= 17;
            current_value %= 256;
        }
        return current_value;
    }

    public static void printHolidayASCIIStringHelperManualArrangementProcedure(Map<String, Integer> focal_lengths, Map<Integer, List<String>> lenses) {
        for (Integer lense: lenses.keySet()) {
            if (lenses.get(lense).size() > 0) {
                System.err.print(String.format("Box %d: ", lense));
                for (String str: lenses.get(lense))
                    System.err.print(String.format("[%s %d] ", str, focal_lengths.get(str)));
                System.err.println();
            }
        }
        System.err.println();
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        int total = 0;
        for (String s: reader.getCodes())
            total += hash(s);
        
        System.out.println(total);

    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Map<String, Integer> focal_lengths = new HashMap<String, Integer>();
        Map<Integer, List<String>> lenses = new HashMap<Integer, List<String>>();
        for (int i=0; i<256; i++) {
            lenses.put(i, new ArrayList<String>());
        }
        

        String label;
        int focal_length;
        for (String s: reader.getCodes())  {
            if (s.contains("-")) {
                label = s.substring(0, s.indexOf("-"));
                lenses.get(hash(label)).remove(label);
                focal_lengths.remove(label);
            }
            else {
                label = s.substring(0, s.indexOf("="));
                focal_length = Integer.parseInt(s.substring(s.indexOf("=")+1));
                if (!lenses.get(hash(label)).contains(label))
                    lenses.get(hash(label)).add(label);
                focal_lengths.put(label, focal_length);
            }
        }

        int total = 0;
        int focusing_power;
        for (String s: focal_lengths.keySet()) {
            focusing_power = 1 + hash(s);
            focusing_power *= 1 + lenses.get(hash(s)).indexOf(s);
            focusing_power *= focal_lengths.get(s);
            total += focusing_power;
        }

        System.out.println(total);
    
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day15/day15_input.txt";

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
