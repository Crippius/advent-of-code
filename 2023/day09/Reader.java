package day09;
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

    public List<Integer> getHistory() throws IOException {
        
        String str = br.readLine();
        if (str == null)
            return null;
        
        List<Integer> history = new ArrayList<Integer>();
        
        for (String s: str.split(" "))
            history.add(Integer.parseInt(s));
        
        return history;
        
    }

}
