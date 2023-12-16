package day11;

import java.util.List;

public class Main {

    public static long getDistance(Coords first, Coords second, List<Coords> empty, long entropy) {
        long distance = 0;
        boolean check;
        for (int i = min(first.getX(), second.getX())+1; i<=max(first.getX(), second.getX()); i++) {
            check = true;
            for (Coords c: empty) {
                if (c.getX() == i) {
                    check = false;
                    break;
                }
            } 
            distance += check ? 1 : entropy;
        }
        for (int i = min(first.getY(), second.getY())+1; i<=max(first.getY(), second.getY()); i++) {
            check = true;
            for (Coords c: empty) {
                if (c.getY() == i) {
                    check = false;
                    break;
                }
            } 
            distance += check ? 1 : entropy;
        }
        return distance;

    }

    private static int min(int x, int y) {
        return x<y ? x:y;
    }

    private static int max(int x, int y) {
        return x>y ? x:y;
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Space space = reader.getSpace();
        List<Coords> empty = space.emptySpace();
        List<Coords> galaxies = space.getGalaxies();

        long total = 0;
        for (int i = 0; i < galaxies.size() - 1; i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                total += getDistance(galaxies.get(i), galaxies.get(j), empty, 2);
            }
        }

        System.out.println(total);



    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Space space = reader.getSpace();
        List<Coords> empty = space.emptySpace();
        List<Coords> galaxies = space.getGalaxies();

        long total = 0;
        for (int i = 0; i < galaxies.size() - 1; i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                total += getDistance(galaxies.get(i), galaxies.get(j), empty, 1000000);
            }
        }

        System.out.println(total);



    }

    public static void main(String[] args) throws Exception {

        String file_name = "day11/day11_input.txt";

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
