package day06;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Reader {

    private final BufferedReader br;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    public List<Race> getRaces() throws IOException {

        String str = br.readLine();
        if (str == null)
            return null;
        str = str.substring(str.indexOf(":")+1);
        List<Long> times = new ArrayList<Long>(); 
        for (String s: str.split(" ")) {
            if (s != "") 
                times.add(Long.parseLong(s));
        }
        str = br.readLine();
        str = str.substring(str.indexOf(":")+1);  
        List<Race> races = new ArrayList<Race>();
        int i=0;
        for (String s: str.split(" ")) {
            if (s != "") {
                races.add(new Race(times.get(i), Long.parseLong(s)));
                i++;
            }
        }
        return races;
    }

    public Race getRace() throws IOException {

        String str = br.readLine();
        if (str == null)
            return null;
        str = str.substring(str.indexOf(":")+1);
        String time = ""; 
        for (String s: str.split(" ")) {
            if (s != "") 
                time += s;
        }
        str = br.readLine();
        str = str.substring(str.indexOf(":")+1);  
        String record = "";
        for (String s: str.split(" ")) {
            if (s != "") 
                record += s;
        }
        return new Race(Long.parseLong(time), Long.parseLong(record));
    }

}