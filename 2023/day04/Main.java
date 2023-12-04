package day04;

import java.util.ArrayList;
import java.util.List;

public class Main {
    
    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        Card curr_card;

        int sum = 0;
        while ((curr_card = reader.getCard()) != null) {
            sum += curr_card.calculateScore();
        }
        System.out.println(sum);
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        List<Card> cards = new ArrayList<Card>();
        Card tmp;
        int[] scratchcards;

        while ((tmp = reader.getCard()) != null)
            cards.add(tmp);
        
        scratchcards = new int[cards.size()];
        for (int i=0; i < scratchcards.length; i++) 
            scratchcards[i] = 1;

        int i = 0;
        for (Card c: cards) {
            for (int j=1; j <= c.getNumWinners(); j++)
                scratchcards[i+j] += scratchcards[i];
            i++;
        }

        int sum = 0;
        for (int z: scratchcards)
            sum += z;
        System.out.println(sum);



        
        



    }

    public static void main(String[] args) throws Exception {

        String file_name = "day04/day04_input.txt";

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
