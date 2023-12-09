package day07;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class HandofCards implements Comparable<HandofCards> {
    
    private List<Character> hand;
    private int money;
    private boolean jolly;


    private int mapper(char x) {
        if (Character.isDigit(x))
            return Integer.parseInt(x+"");
        if (x == 'T')
            return 10;
        if (x == 'J') {
            if (jolly)
                return 1;
            else
                return 11;
        }

        if (x == 'Q')
            return 12;
        if (x == 'K')
            return 13;
        if (x == 'A')
            return 14;
        return -1;
    }

    public HandofCards(List<Character> hand, int money, boolean jolly) {
        this.jolly = jolly;
        this.hand = hand;
        this.money = money;
        if (hand.size() != 5) {
            hand = null;
            money = -1;
        }
    }
    
    public int getMoney() {
        return money;
    }


    private Map<Character, Integer> getDistinct() {
        Map<Character, Integer> seen = new HashMap<Character, Integer>();

        for (Character c: hand) {
            if(!seen.keySet().contains(c))
                seen.put(c, 0);
            seen.put(c, seen.get(c)+1);
        }
        return seen;
    }

    private int countDistinct() {
        return getDistinct().size();   
    }


    public boolean isFiveofaKind() {
        if (countDistinct() == 1)
            return true;
        if (jolly)    
            if (countDistinct() == 2 && getDistinct().containsKey('J'))
                return true;
        return countDistinct() == 1;
    }

    public boolean isFourofaKind() {
        Map<Character, Integer> count = getDistinct();

        if (count.size() == 2)
            for (Character c: count.keySet())
                if (count.get(c) == 4)
                    return true;
        if (jolly) {
            if (count.size() == 3 && count.containsKey('J')) {
                int jollies = count.get('J');
                for (Character c: count.keySet())
                    if (c != 'J' && count.get(c)+jollies == 4)
                        return true;
            }
        }
        return false;
    }

    public boolean isFullHouse() {
        if (countDistinct() == 2 && !isFourofaKind())
            return true;
        Map<Character, Integer> count = getDistinct();
        if (jolly) {
            if (count.size() == 3 && count.containsKey('J')) {
                Character first = '_';
                Character second = '_';

                for (Character c: count.keySet()) {
                    if (c != 'J') {
                        if (first == '_')
                            first = c;
                        if (c != first && second == '_')
                            second = c;
                    }
                }
                int jollies = count.get('J');
                for (int i = 0; i<=jollies; i++) {
                    if (count.get(first)+i == 3 && count.get(second)+jollies-i == 2)
                        return true;
                    if (count.get(second)+i == 3 && count.get(first)+jollies-i == 2)
                        return true;
                }       
            }
        }
        return false; 
    }

    public boolean isThreeofaKind() {
        Map<Character, Integer> count = getDistinct();
        if (count.size() == 3) {
            for (Character c: count.keySet()) 
                if (count.get(c) == 3)
                    return true;
        }
        if (jolly) {
            if (count.size() == 4 && count.containsKey('J')) {
                int jollies = count.get('J');
                for (Character c: count.keySet())
                    if (c != 'J' && count.get(c)+jollies == 3)
                        return true;
            }

        }
        return false;
    }

    public boolean isTwoPair() {
        if (countDistinct() == 3 && !isThreeofaKind())
            return true;
        Map<Character, Integer> count = getDistinct();
        if (jolly) {
            int total = 0;
            for (Character c: count.keySet()) {
                if (count.get(c) >= 2)
                    total += 1;
            }
            if (count.keySet().contains('J'))
                total += count.get('J');
            if (total >= 2)
                return true;
        } 
        return false;
    }

    public boolean isOnePair() {
        Map<Character, Integer> count = getDistinct();

        if (count.size() == 4) {
            for (Character c: count.keySet()) 
                if (count.get(c) == 2)
                    return true;
        }
        if (jolly) {
            if (count.size() == 5 && count.containsKey('J'))
                return true;
        }
        return false;
    }

    public boolean isHighCard() {
        return true;
    }

    private int stalemateBreaker(HandofCards other) {
        for (int i=0; i<hand.size(); i++) {
            if (mapper(hand.get(i)) != mapper(other.hand.get(i))) {
                return (mapper(hand.get(i)) - mapper(other.hand.get(i)));
            }
        }
        return 0;
    }

    @Override
    public String toString() {
        String print = "";
        for (Character c: hand) {
            print += c+"";
        }
        print += " ";
        print += Integer.toString(money);
        return print;
    }

    @Override
    public int compareTo(HandofCards other) {
        boolean[] this_methods = {isFiveofaKind(), isFourofaKind(), isFullHouse(), isThreeofaKind(), isTwoPair(), isOnePair(), isHighCard()};
        boolean[] other_methods = {other.isFiveofaKind(), other.isFourofaKind(), other.isFullHouse(), other.isThreeofaKind(), other.isTwoPair(), other.isOnePair(), other.isHighCard()};

        for (int i=0; i<this_methods.length; i++) {
            if (this_methods[i] == true && this_methods[i] == other_methods[i])
                return stalemateBreaker(other);
            if (this_methods[i] == true)
                return 1;
            if (other_methods[i] == true)
                return -1;
        }
        return 0;
    }
}
