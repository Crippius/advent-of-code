package day14;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Platform implements Cloneable {

    private int row_length;
    private int column_length;
    private List<Rock> rocks;
    

    public Platform(List<Rock> rocks, int row_length, int column_length) {
        this.rocks = rocks;
        this.row_length = row_length;
        this.column_length = column_length;
        
    }

    public List<Rock> getRocks() {
        return rocks;
    }

    public int getColumnLength() {
        return column_length;
    }

    public int getRowLength() {
        return row_length;
    }


    private void sort(Character direction) {
        Collections.sort(rocks, new RockComparator(direction));
    }

    public boolean contains(Rock rock) {
        for (Rock r: rocks) 
            if (r.equals(rock))
                return true;

        return false;
    }

    private boolean adjacent(Rock rock, Character direction) {
        int x = -1;
        int y = -1;

        if (direction == 'N') {
            x = rock.getX(); 
            y = rock.getY()-1;
        }
        else if (direction == 'E') {
            x = rock.getX()+1; 
            y = rock.getY();
        }
        else if (direction == 'W') {
            x = rock.getX()-1; 
            y = rock.getY();
        }
        else if (direction == 'S') {
            x = rock.getX(); 
            y = rock.getY()+1;
        }
        for (Rock r : rocks)
            if (r.equals(x, y)) {
                return true;
            }

        return false;

    }

    public void tilt(Character direction) {
        
        if (direction == 'N') {
            sort((Character) direction);
            for (Rock r : rocks) {
                if (r.isMovable()) 
                    while (r.getY() > 0 && !adjacent(r, direction)) {
                        r.setXY(r.getX(), r.getY()-1);
                    }
            }
        }
        else if (direction == 'W') {
            sort((Character) direction);
            for (Rock r : rocks) {
                if (r.isMovable()) 
                    while (r.getX() > 0 && !adjacent(r, direction)) {
                        r.setXY(r.getX()-1, r.getY());
                    }
            }
        }
        else if (direction == 'S') {
            sort((Character) direction);
            for (Rock r : rocks) {
                if (r.isMovable()) 
                    while (r.getY() < column_length && !adjacent(r, direction)) {
                        r.setXY(r.getX(), r.getY()+1);
                    }
            }
        }
        else if (direction == 'E') {
            sort((Character) direction);
            for (Rock r : rocks) {
                if (r.isMovable()) 
                    while (r.getX() < row_length && !adjacent(r, direction)) {
                        r.setXY(r.getX()+1, r.getY());
                    }
            }
        }
    }

    public void spin() {
        Character[] directions = {'N', 'W', 'S', 'E'};
        for (Character dir: directions) {
                tilt(dir);
            }
    }

    public Platform clone() throws CloneNotSupportedException {
        Platform clonedPlatform = (Platform) super.clone();

        List<Rock> clonedRocks = new ArrayList<>();
        for (Rock rock : rocks) {
            if (rock.isMovable())
                clonedRocks.add(new RoundRock(rock.getX(), rock.getY()));
            else
                clonedRocks.add(new CubeRock(rock.getX(), rock.getY()));
        }
        clonedPlatform.rocks = clonedRocks;

        return clonedPlatform;
    }

    @Override
    public String toString() {
        String print = "";
        boolean found;
        Rock found_rock = null;
        for (int y=0; y<=column_length; y++) {
            for (int x=0; x<=row_length; x++) {
                found = false;
                for (Rock r: rocks)
                    if (r.equals(x, y)) {
                        found_rock = r;
                        found = true;
                        break;
                    }
                
                print += found ? (found_rock.isMovable() ? "O" : "#") : ".";
            }
            print += "\n";
        }
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

        Platform other = (Platform) obj;
        for (Rock my_r: rocks) {
            boolean found = false;
            for (Rock other_r : other.rocks) {
                if (my_r.getX() == other_r.getX() && my_r.getY() == other_r.getY()) {
                    found = true;
                }
            }
            if (!found) {
                return false;
            }
        }
        return (rocks.size() == other.rocks.size());
    }

}
