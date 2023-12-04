package day04;

import java.io.*;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public Card getCard() throws IOException {

        Card card = new Card();
        String[] nums_str;
        String str = br.readLine();
        if (str == null)
            return null;
        
        nums_str = str.substring(str.indexOf(":")+1, str.indexOf("|")).split(" ");
        for (String s: nums_str) {
            if (s == "")
                continue;
            card.addWinningNumber(Integer.parseInt(s));
        }
        
        nums_str = str.substring(str.indexOf("|")+1).split(" ");
        for (String s: nums_str) {
            if (s == "")
                continue;
            card.addMyNumber(Integer.parseInt(s));
        }
        
        return card;
    }
}