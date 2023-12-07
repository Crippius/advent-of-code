package day05;

import java.util.LinkedList;
import java.util.List;

public class BigMapper {
    private List<Mapper> bigmap;
    
    public BigMapper() {
        bigmap = new LinkedList<Mapper>();
    }
    
    public void addMapper(Mapper mapper) {
        bigmap.addFirst(mapper);
    }

    public long map(long x) {
        long result = x;
        for (Mapper mapper: bigmap)
            result = mapper.map(result);
        return result;
    }

}
