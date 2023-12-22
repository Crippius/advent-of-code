package day17;


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

    public List<List<Integer>> getCity() throws IOException {

        List<List<Integer>> city = new ArrayList<List<Integer>>();
        List<Integer> row;

        String str;
        while ((str = br.readLine()) != null) {
            row = new ArrayList<Integer>();
            for (Character c: str.toCharArray()) 
                row.add(Integer.parseInt(c+""));
            city.add(row);
        }
        

        return city;
    }
}
