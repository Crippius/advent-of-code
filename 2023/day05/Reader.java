package day05;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Reader {

    private final BufferedReader br;

    private Evolution state;

    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
        state = Evolution.BAG;

        
    }

    public Evolution getState() {
        return state;
    }

    public List<Long> getSeeds() throws IOException {
        String str = br.readLine();
        
        List<Long> seeds = new ArrayList<Long>();

        if (str == null)
            return null;
        if (state != Evolution.BAG)
            return null;
        
        str = str.substring(str.indexOf(":")+1);
        List<Long> split_str = new ArrayList<Long>();
        for (String s: str.split(" ")) {
            if (s != "")
                split_str.add(Long.parseLong(s));
        }
        for (long s: split_str) 
            seeds.add(s);

        br.readLine();
        state = state.nextState();
        return seeds;
        
    }

public List<Range> getSeedsRange() throws IOException {
        String str = br.readLine();
        
        List<Range> seeds = new ArrayList<Range>();

        if (str == null)
            return null;
        if (state != Evolution.BAG)
            return null;
        
        str = str.substring(str.indexOf(":")+1);
        List<Long> split_str = new ArrayList<Long>();
        for (String s: str.split(" ")) {
            if (s != "")
                split_str.add(Long.parseLong(s));
        }

        for (int i=0; i<split_str.size(); i+=2)
            seeds.add(new Range(split_str.get(i), split_str.get(i)+split_str.get(i+1)));


        br.readLine();
        state = state.nextState();
        return seeds;
    }


    public Mapper getMapper(boolean reverse) throws IOException {
        
        if (state == Evolution.BAG)
            return null;
        
        br.readLine();

        Mapper map = new Mapper();
        String str;
        String[] split_str = new String[5];
        long destination;
        long source;
        long length;

        while (true) {
            str = br.readLine();
            if (str == null || str.length() < 3) {
                break;
            }
            split_str = str.split(" ");

            destination = Long.parseLong(split_str[0]);
            source = Long.parseLong(split_str[1]);
            length = Long.parseLong(split_str[2]);

            map.addMap(destination, source, length, reverse);
        }  

        state = state.nextState();
        
        return map;
    }

    public BigMapper getBigMapper() throws IOException {
        
        if (state == Evolution.BAG)
            return null;
        
        BigMapper bigmapper = new BigMapper();

        while (state != Evolution.LOCATION) {
            bigmapper.addMapper(getMapper(true));
        }

        return bigmapper;

    } 

}