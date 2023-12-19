package day14;

import java.util.Objects;

public class Rock {

    private Coords xy;
    protected boolean is_movable;

    public Rock(int x, int y) {
        this.xy = new Coords(x, y);
    }

    public int getX() {
        return xy.getX();
    }

    public int getY() {
        return xy.getY();
    }

    public void setXY(Coords xy) {
        this.xy = xy;
    }

    public void setXY(int x, int y) {
        this.xy.setXY(x, y);
    }

    public boolean isMovable() {
        return is_movable;
    }

    public boolean equals(int x, int y) {
        return xy.getX() == x && xy.getY() == y;
    }

    @Override
    public String toString() {
        
        return xy.toString();
    }

    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;

        Rock other = (Rock) obj;
        return this.xy.equals(other.xy);
    }

    @Override
    public int hashCode() {
        return Objects.hash(xy);
    }

    
}
