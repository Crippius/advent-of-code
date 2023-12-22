package day17;

import java.util.Objects;

public class Coords {
    
    private int x;
    private int y;

    public Coords(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Coords(Coords pos) {
        this.x = pos.x;
        this.y = pos.y;
    }

    public Coords sum(Coords c) {
        
        return new Coords(this.x + c.x, this.y + c.y);
    }

    public Coords sum(int x, int y) {
        
        return new Coords(this.x + x, this.y + y);
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "(" + x + ", " + y + ")";
    }
    public boolean equals(int x, int y) {
        return this.x == x &&
               this.y == y;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null) 
            return false;
        if (getClass() != obj.getClass())
            return false;

        Coords other = (Coords) obj;
        return this.x == other.x &&
               this.y == other.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}
