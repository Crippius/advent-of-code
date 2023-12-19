package day13;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Reader {   

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public Mirror getMirror() throws IOException {;

        String str;
        int row_length = 0;
        int column_length = 0;
        List<Character[]> table = new ArrayList<Character[]>();
        while ((str = br.readLine()) != null && str.length() > 1) {
            Character[] row = new Character[str.length()]; 
            row = str.chars().mapToObj(c -> (char) c).toArray(Character[]::new);
            table.add(row);
            row_length = str.length();
            column_length++;
        }
        if (str == null && column_length == 0)
            return null;
        
        Character[][] mirror= table.toArray(new Character[0][]);

        return new Mirror(mirror, row_length, column_length);
    }

}
