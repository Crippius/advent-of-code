package day18;


import java.util.List;

public class Main {

    // Inner area formula: Shoelace formula
    // Total area: Picks theorem
    public static long getArea(List<Coords> vertices) {

        long perimeter = 0;
        long inner_area = 0;
        long xi, yi, xi1, yi1;
        for (int i=0; i<vertices.size()-1; i++) {
            xi = vertices.get(i).getX();
            yi = vertices.get(i).getY();
            xi1 = vertices.get(i+1).getX();
            yi1 = vertices.get(i+1).getY();

            inner_area += xi*yi1 - xi1*yi;
            perimeter += Math.abs(xi-xi1)+Math.abs(yi-yi1);
        }
        xi = vertices.get(vertices.size()-1).getX();
        yi = vertices.get(vertices.size()-1).getY();
        xi1 = vertices.get(0).getX();
        yi1 = vertices.get(0).getY();

        inner_area += xi*yi1 - xi1*yi;
        perimeter += Math.abs(xi-xi1)+Math.abs(yi-yi1);

        return (Math.abs(inner_area) + perimeter) / 2 + 1;    
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  
        
        List<Coords> vertices = reader.getDigPlan(false);

        System.out.println(getArea(vertices));


    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);
        
        List<Coords> vertices = reader.getDigPlan(true);

        System.out.println(getArea(vertices));

        
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day18/day18_input.txt";

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
