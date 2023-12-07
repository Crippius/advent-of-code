package day05;

import java.util.HashMap;
import java.util.Map;

public class Mapper {
    
    Map<Range, Long> map;
    
    public Mapper() {
        map = new HashMap<Range, Long>();
    }
    
    public void addMap(long destination, long source, long length, boolean reverse) {

        if (!reverse) { 
            Range range = new Range(source, source+length);
            map.put(range, destination);
        }
        else {
            Range range = new Range(destination, destination+length);
            map.put(range, source);
        }
        
    }

    private long getResult(Range r, long x) {
        return map.get(r) + (x-r.getStart());
    }

    public long map(long x) {
        for (Range r: map.keySet()) {
            if (r.isInRange(x))
                return getResult(r, x);
        }
        return x;
    }

    @Override
    public String toString() {
        String print = "";
        for (Range r: map.keySet()) {
            print += r;
        }
        return print;
    }


}
