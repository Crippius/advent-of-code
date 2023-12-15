package day10;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Reader {   

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public Pipeline getPipeline() throws IOException {
        
        Pipeline pipeline = new Pipeline();
        
        String str;

        int x = 0;
        int y = 0;
        while ((str = br.readLine()) != null) {
            x = 0;
            for (Character c: str.toCharArray()) {
                if (c != '.' && c != '\n')
                    pipeline.addPipe(new Coords(x, y), c);
                x++;
            }
            y++;
        }
        return pipeline;
        
    }

}
