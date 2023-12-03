package day03;

import java.io.*;
import java.util.*;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public List<List<Character>> GetTable() throws IOException {

        List<List<Character>> table = new ArrayList<List<Character>>();
        List<Character> row;
        String str;
        while ((str = br.readLine()) != null) {
            row = new ArrayList<Character>();
            for (Character c: str.toCharArray())
                row.add(c);
            table.add(row);
        }
        
        return table;
    }
}