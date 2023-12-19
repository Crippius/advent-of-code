package day13;

public class Main {

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Mirror mirror;
        int total = 0;
        while ((mirror = reader.getMirror()) != null) {
            total += mirror.findReflection(false);
        }

        System.out.println(total);
    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Mirror mirror;
        int total = 0;
        while ((mirror = reader.getMirror()) != null) {
            mirror.findReflection(true);
            mirror.fixError();
            total += mirror.findReflection(true);
        }

        System.out.println(total);


    }

    public static void main(String[] args) throws Exception {

        String file_name = "day13/day13_input.txt";

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
