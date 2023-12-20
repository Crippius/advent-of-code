package day16;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public Cave getCave() throws IOException {

        int x = 0;
        int y = 0;
        Map<Coords, Character> mirrors = new HashMap<Coords, Character>();

        String str;
        while ((str = br.readLine()) != null) {
            x = 0;
            for (Character c: str.toCharArray()) {
                if (c != '.')
                    mirrors.put(new Coords(x, y), c);
                x++;
            }
            y++;
        }
        

        return new Cave(mirrors, x-1, y-1);
    }

}
