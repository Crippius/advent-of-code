package day02;

import java.io.*;
import java.util.*;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    private Color mapper(String color) {
        if (color.startsWith("b"))
            return Color.BLUE;
        if (color.startsWith("r"))
            return Color.RED;
        if (color.startsWith("g"))
            return Color.GREEN;
        else
            return Color.NULL;   
    }

    public List<Map<Color, Integer>> GetLine() throws IOException {

        List<Map<Color, Integer>> game = new ArrayList<Map<Color, Integer>>();
        String round[];
        String colors[];
        String num_col[];
        Map<Color, Integer> round_col;
        String str;

        str = br.readLine();
        if (str == null) {
            return null;
        }
            
        str = str.substring(str.indexOf(":")+1);
        round = str.split(";");
        int i = 0;
        for (String s : round) {
            colors = s.split(",");
            for (String c : colors) {
                num_col = c.split(" ");
                round_col = new HashMap<>();
                round_col.put(mapper(num_col[2]), Integer.parseInt(num_col[1]));
                if (mapper(num_col[2]) == Color.NULL)
                    System.err.println(num_col[2]);
                game.add(i, round_col);
                i++;  
            }
            
        }
        
        return game;
        
    }


    public Map<Color, Integer> GetMin() throws IOException {

        Map<Color, Integer> game = new HashMap<>();
        String round[];
        String colors[];
        String num_col[];
        String str;

        str = br.readLine();
        if (str == null) {
            return null;
        }
        
        for (Color c: Color.values()) {
            game.put(c, 1);
        }

        str = str.substring(str.indexOf(":")+1);
        round = str.split(";");
        for (String s : round) {
            colors = s.split(",");
            for (String c : colors) {
                num_col = c.split(" ");
                if (Integer.parseInt(num_col[1]) > game.get(mapper(num_col[2])))
                    game.put(mapper(num_col[2]), Integer.parseInt(num_col[1]));
            }
            
        }
        return game;
    }
}
