package day04;
import java.util.*;

public class Card {

    private static int totalID = 0;
    private int cardID;
    
    private List<Integer> winning_nums;

    private List<Integer> my_nums;

    public Card() {
        
        totalID++;
        cardID = totalID;

        winning_nums = new ArrayList<Integer>();
        my_nums = new ArrayList<Integer>();

    }

    public int getID() {
        return cardID;
    }

    public void addWinningNumber(int num) {
        winning_nums.add(num);
    }

    public void addMyNumber(int num) {
        my_nums.add(num);
    }


    public int calculateScore() {

        int total = getNumWinners();

        return total == 0 ? 0 : (int) Math.pow(2, total-1);

    }

    public int getNumWinners() {
        
        int total = 0;
        for (int num : my_nums) {
            if (winning_nums.contains(num))
                total++;
        }
        return total;
    }

    @Override
    public String toString() {
        String print = "Card ";
        print += String.format("%d: ", cardID);
        for (int num : winning_nums)
            print += String.format("%d ", num);
        print += "| ";
        for (int num : my_nums)
            print += String.format("%d ", num);       

        return print;
    }
}
