package day17;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.TreeSet;

public class Main {

    private static Node min(List<Node> nodes) {
        Node minimium = nodes.get(0);
        for (Node n: nodes) 
            if (n.getDistance() < minimium.getDistance())
                minimium = n;

        return minimium;

    }

    private static Coords[] dirs_coords = {new Coords(0, -1), new Coords(-1, 0), new Coords(0, +1), new Coords(+1, 0)};
    
    private static Character[] dirs = {'N', 'W', 'S', 'E'};


    private static boolean inside(Coords pos, int row_length, int column_length) {
        return 0 <= pos.getX() && pos.getX() < row_length &&
               0 <= pos.getY() && pos.getY() < column_length; 
    }

    private static List<Node> getNewNodes(Node n, List<List<Integer>> city, Set<Node> visited, int min_turn, int max_turn) {

        int row_length = city.get(0).size();
        int column_length = city.size();

        List<Node> new_nodes = new ArrayList<Node>();

        Coords[] turns = new Coords[2];
        Character[] directions = new Character[2];
        if (n.getDir() == 'N' || n.getDir() == 'S') {
            turns[0] = dirs_coords[1]; turns[1] = dirs_coords[3];
            directions[0] = dirs[1]; directions[1] = dirs[3];
        }
        else if (n.getDir() == 'W' || n.getDir() == 'E') {
            turns[0] = dirs_coords[0]; turns[1] = dirs_coords[2];
            directions[0] = dirs[0]; directions[1] = dirs[2];
        }
        else {
            turns = dirs_coords;
            directions = dirs;
        }

        for (int dir = 0; dir<turns.length; dir++) {
            Coords c = new Coords(n.getPos());
            int dist = n.getDistance();
            for (int i=1; i<max_turn+1; i++) {
                c = c.sum(turns[dir]);
                if (inside(c, row_length, column_length)) {
                    dist += city.get(c.getY()).get(c.getX());
                    if (i >= min_turn)
                        new_nodes.add(new Node(c, directions[dir], n.getMoves(), dist, n));
                }
            }


        }

        // int new_distance = n.getDistance()+city.get(n.getPos().getY()).get(n.getPos().getX());
        // for (int i=0; i<dirs.length; i++) {
        //     if (n.getDir() != dirs[i]) // Get correct direction
        //         continue;

        //     if (n.getMoves() < min_turn - 1) { // Not possible to turn
        //         if (!inside(n.getPos().sum(dirs_coords[i]), row_length, column_length)) // New position in bounds
        //             continue;
        //         new_nodes.add(new Node(new Coords(n.getPos().sum(dirs_coords[i])), // Position
        //                       dirs[i], // Direction
        //                       n.getMoves()+1, // Number of Moves
        //                       new_distance, // Distance
        //                       n)); // Prev
        //     }
        //     else {
        //         for (int j=0; j<dirs.length; j++) {
        //             if (dirs[j] == dirs[(i+2)%4]) // Not opposite direction
        //                 continue;
        //             if (dirs[j] == dirs[i] && n.getMoves() >= max_turn-1) // Can't go straight
        //                 continue;
        //             if (!inside(n.getPos().sum(dirs_coords[j]), row_length, column_length))  // New position in bounds
        //                 continue;
        //             new_nodes.add(new Node(new Coords(n.getPos().sum(dirs_coords[j])), // Position
        //                           dirs[j], // Direction
        //                           n.getDir() == dirs[j] ? n.getMoves()+1 : 0, // Number of Moves
        //                           new_distance, // Distance
        //                           n)); // Prev
        //         }
        //     }
            
        // }
        
        return new_nodes;
    }

    public static int shortestPath(List<List<Integer>> city, int min_turn, int max_turn) {

        Set<Node> visited = new HashSet<Node>();

        PriorityQueue<Node> to_check = new PriorityQueue<Node>();
        to_check.add(new Node(new Coords(0, 0), 'O', 0, 0, null));

        Coords final_cell = new Coords(city.get(0).size()-1, city.size()-1);
        Node curr;

        while (to_check.size() > 0) {
            
            curr = to_check.poll();
            to_check.remove(curr);

            if (curr.getPos().equals(final_cell)) {

                return curr.getDistance();
            }
            if (visited.contains(curr))
                continue;
            visited.add(curr);

            for (Node n: getNewNodes(curr, city, visited, min_turn, max_turn))
                to_check.add(n);
            
        }

        return -1;
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  
        
        List<List<Integer>> city = reader.getCity();

        System.out.println(shortestPath(city, 1, 3));

    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);

        List<List<Integer>> city = reader.getCity();

        System.out.println(shortestPath(city, 4, 10));

    }

    public static void main(String[] args) throws Exception {

        String file_name = "day17/day17_input.txt";

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
