package day12;

import java.util.List;

public class Row {
    private List<Character> disp;
    private List<Integer> config;


    public Row(List<Character> disp, List<Integer> config) {
        this.disp = disp;
        this.config = config;
    }

    public List<Character> getDisposition() {
        return disp;
    }

    public List<Integer> getConfiguration() {
        return config;
    }    
}
