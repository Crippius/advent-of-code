package day14;

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

    public Platform getPlatform() throws IOException {;

        String str;
        int x = 0;
        int y = 0;
        
        List<Rock> table = new ArrayList<Rock>();
        while ((str = br.readLine()) != null) {
            x = 0;
            for (Character c : str.toCharArray()) {
                if (c == 'O')
                    table.add(new RoundRock(x, y));
                else if (c == '#')
                    table.add(new CubeRock(x, y));
                x++;
            }
            y++;
        }


        return new Platform(table, x-1, y-1);
    }

}
