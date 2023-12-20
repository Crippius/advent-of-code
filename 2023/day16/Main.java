package day16;

public class Main {

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  
        
        Cave cave = reader.getCave();

        System.out.println(cave);
        System.out.println(cave.getTotalEnergizedTiles(new Coords(0, 0), 'E'));

    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        Cave cave = reader.getCave();

        int max = 0;
        int tmp;
        for (int i=0; i<=cave.getRowLength(); i++) {
            tmp = cave.getTotalEnergizedTiles(new Coords(i, 0), 'S');
            if (tmp > max)
                max = tmp;
            
            tmp = cave.getTotalEnergizedTiles(new Coords(i, cave.getColumnLength()), 'N');
            if (tmp > max)
                max = tmp;
        }

        System.out.println(max);
    
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day16/day16_input.txt";

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
