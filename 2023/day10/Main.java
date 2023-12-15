package day10;

import java.util.List;

public class Main {



    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Pipeline pipeline = reader.getPipeline();
        List<Coords> pipes = pipeline.findConnection();
        if (pipes == null) {
            System.err.println("uffi");
            return;
        }
        
        System.out.println(pipes.size()/2);

    }


    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        Pipeline pipeline = reader.getPipeline();
        List<Coords> pipes = pipeline.findConnection();
        if (pipes == null) {
            System.err.println("uffi");
            return;
        }
        int min_x = Integer.MAX_VALUE, min_y = Integer.MAX_VALUE, max_x = 0, max_y = 0;
        for (Coords c: pipes) {
            if (c.getX() < min_x)
                min_x = c.getX();
            if (c.getX() > max_x)
                max_x = c.getX();
            if (c.getY() < min_y)
                min_y = c.getY();
            if (c.getY() > max_y)
                max_y = c.getY();
        } 
        int inside_cells = 0; 
        boolean inside;
        String flippers = "|JLS";
        Coords checker = new Coords(min_x, min_y);
        for (int y = min_y; y <= max_y; y++) {
            inside = false;
            for (int x = min_x; x <= max_x; x++) {
                checker.setXY(x, y);
                if (pipes.contains(checker)) {
                    if (flippers.contains(String.valueOf(pipeline.getPipe(checker)))) 
                        inside = !inside;
                    continue;
                }
                
                if (inside) {
                    inside_cells++;
                }
            }
        }
        System.out.println(inside_cells);
        

    }

    public static void main(String[] args) throws Exception {

        String file_name = "day10/day10_input.txt";

        try {
            part1(file_name);
        } catch (Exception e) {
            System.err.println("Part 1 Failed " + e);
        }
        try {
            part2(file_name);
        } catch (Exception e) {
            System.err.println("Part 2 Failed " + e);
        }

    }   
}
