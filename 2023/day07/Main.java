package day07;

import java.util.List;
import java.util.Collections;

public class Main {
    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<HandofCards> bets = reader.getBets(false);
        Collections.sort(bets);
        int rank = 1;
        int total_winnings = 0;
        for (HandofCards bet: bets) {
            total_winnings += rank*bet.getMoney();
            rank++;
        }
        System.out.println(total_winnings);
            
    
        
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<HandofCards> bets = reader.getBets(true);
        Collections.sort(bets);
        int rank = 1;
        int total_winnings = 0;
        for (HandofCards bet: bets) {
            total_winnings += rank*bet.getMoney();
            rank++;
        }
        System.out.println(total_winnings);

    }

    public static void main(String[] args) throws Exception {

        String file_name = "day07/day07_input.txt";

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
