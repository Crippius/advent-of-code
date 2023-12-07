package day05;

public class Range {
    
    private long start;
    private long end;

    public Range(long start, long end) {
        this.start = start;
        this.end = end;
    }

    public boolean isInRange(long x) {
        return x >= start && x < end;
    }

    public long getStart() {
        return start;
    }
    public long getEnd() {
        return end;
    }

    @Override
    public String toString() {
        return String.format("(%d, %d)\n", getStart(), getEnd());
    }
}
