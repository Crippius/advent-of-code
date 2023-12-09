package day07;

import java.io.BufferedReader;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Reader {   
    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }
    public List<HandofCards> getBets(boolean jolly) throws IOException {

        String str;
        String[] split_str = new String[2];
        
        List<HandofCards> bets = new ArrayList<HandofCards>(); 
        while((str = br.readLine()) != null) {
            split_str = str.split(" ");
            List<Character> hand = new ArrayList<Character>();
            for (Character c: split_str[0].toCharArray())
                hand.add(c);
            bets.add(new HandofCards(hand, Integer.parseInt(split_str[1]), jolly));
            
        }
        return bets;
    }
}
