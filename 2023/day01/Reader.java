package day01;


import java.io.*;
import java.util.*;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }
    public List<String> GetInfo() throws IOException {
        List<String> list =  new ArrayList<String>();
        String str;
        while ((str = br.readLine()) != null) {
            list.add(str);
        }
        return list;
        
    }
}
