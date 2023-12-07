package day05;

import java.util.List;

public class Main {
    
    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Long> seeds = reader.getSeeds();
        Mapper map;

        while (reader.getState() != Evolution.LOCATION) {
            map = reader.getMapper(false);
            for (int i=0; i<seeds.size(); i++) {
                seeds.set(i, map.map(seeds.get(i)));
            }
        }
        long min = seeds.get(0);
        for (long seed: seeds) {
            if (seed < min) {
                min = seed;
            }
        }
        System.out.println(min);
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Range> seeds = reader.getSeedsRange();
        BigMapper bigmap = reader.getBigMapper();

        int i=0;
        boolean found = false;

        while (!found) {
            for (Range r:seeds) {
                if (r.isInRange(bigmap.map(i))) {
                    found = true;
                    break;
                }
            }
            i++;
        }
        System.out.println(i-1);
    }


    public static void main(String[] args) throws Exception {

        String file_name = "day05/day05_input.txt";

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
