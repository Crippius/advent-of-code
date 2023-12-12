package day08;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Reader {   

    private final BufferedReader br;
    private int state;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
        state = 0;
    }

    public List<Integer> getInstructions() throws IOException {
        if (state == 1)
            return null;
        
        List<Integer> instr = new ArrayList<Integer>();

        for (Character c: br.readLine().toCharArray()) {
            if (c == 'R')
                instr.add(1);
            if (c == 'L')
                instr.add(0);
        }
        state = 1;
        br.readLine();
        return instr;
        
    }
    
    
    
    public Network getNetwork() throws IOException {
        if (state == 0)
            return null;
        

        Network net = new Network();
        String str;
        
        while ((str = br.readLine()) != null) {
        net.addNode(str.substring(0, 3), 
                        str.substring(7, 10), 
                        str.substring(12, 15));
        }

        state = 2;
        return net;
        
    }
}
