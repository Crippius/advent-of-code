package day09;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static List<Integer> transition(List<Integer> prev_it) {
        List<Integer> new_it = new ArrayList<>();
        for (int i=0; i<prev_it.size()-1; i++) 
            new_it.add(prev_it.get(i+1)-prev_it.get(i));
        return new_it;
    }

    public static boolean isAllZero(List<Integer> lst) {
        for (int n: lst)
            if (n != 0)
                return false;
        return true;
    } 


    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        List<Integer> history;
        int total = 0;
        int sum;
        while ((history = reader.getHistory()) != null) {
            sum = 0;
            while (history.size() > 0 && !isAllZero(history)) {
                sum += history.get(history.size()-1);
                history = transition(history);
            }
            total += sum;
        }
        System.out.println(total);
    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<Integer> history;
        List<Integer> firsts = new LinkedList<Integer>();
        int total = 0;
        int sum;
        while ((history = reader.getHistory()) != null) {
            firsts.clear();
            while (history.size() > 0 && !isAllZero(history)) {
                firsts.addFirst(history.get(0));
                history = transition(history);
                
            }
            sum = 0;
            for (int n : firsts) {
                sum = n - sum;
            }
            total += sum;
        }
        System.out.println(total);
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day09/day09_input.txt";

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