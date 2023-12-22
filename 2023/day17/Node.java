package day17;

import java.util.Objects;

public class Node implements Comparable<Node>{

    private Coords pos;
    private Character dir;
    private int moves;
    private int distance;
    private Node prev;
    
    public Node(Coords pos, Character dir, int moves, int distance, Node prev) {
        this.pos = pos;
        this.dir = dir;
        this.moves = moves;
        this.distance = distance;
        this.prev = prev;
    }

    public Coords getPos() {
        return pos;
    }

    public Character getDir() {
        return dir;
    }

    public int getDistance() {
        return distance;
    }

    public int getMoves() {
        return moves;
    }

    public Node getPrev() {
        return prev;
    }

    public int compareTo(Node other) {
        return this.distance - other.distance;
    }

    @Override
    public String toString() {
        String print = "Node ";
        print += pos + ", ";
        print += "Distance " + distance + ", ";
        print += "Moves " + moves + ", ";
        print += "Direction " + dir+ ", ";
        print += "Prev " + (prev == null ? " " : (prev.pos)+""+(prev.dir));

        return print;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null) 
            return false;
        if (getClass() != obj.getClass())
            return false;

        Node other = (Node) obj;
        return this.pos.equals(other.pos) &&
               this.dir == other.dir;
    }

    @Override
    public int hashCode() {
        return Objects.hash(pos, dir);
    }
}
