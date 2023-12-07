package day06;

import java.util.List;

public class Main {
    
    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Race> races = reader.getRaces();
        int total = 1;
        for (Race race: races) {
            int possible_wins = 0;
            for (int i=1; i<race.getTime(); i++) {
                if (i*(race.getTime()-i) > race.getRecord())
                    possible_wins += 1;
            }

            total *= possible_wins;
        }
        System.out.println(total);
        
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        Race race = reader.getRace();

        long min_time = 0;
        long max_time = 0;
        
        long i = 1;
        while (i*(race.getTime()-i) <= race.getRecord())
            i++;
        min_time = i;
        i = race.getTime();
        while (i*(race.getTime()-i) <= race.getRecord())
            i--;
        max_time = i+1;
        System.out.println(max_time-min_time);

        

    }

    public static void main(String[] args) throws Exception {

        String file_name = "day06/day06_input.txt";

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
