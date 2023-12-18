package day12;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Reader {   

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public Row getRow(boolean unfolded) throws IOException {;
        
        String str = br.readLine();

        if (str == null)
            return null;

        List<Character> disp = new ArrayList<Character>();
        for (int i=0; i<(unfolded ? 5:1); i++) {
            if (i != 0)
                disp.add('?');
            for (Character c: str.split(" ")[0].toCharArray()) 
                disp.add(c);
        }

        List<Integer> config = new ArrayList<Integer>();
        
        for (int i=0; i<(unfolded ? 5:1); i++) {
            for (Integer n: Arrays.stream(str.split(" ")[1].split(",")).mapToInt(Integer::parseInt).toArray()) 
                config.add(n);
        }

        return new Row(disp, config);
    }

}
