package day11;

import java.util.ArrayList;
import java.util.List;

public class Space {

    List<Coords> galaxies;
    int max_x, max_y;

    public Space() {
        galaxies = new ArrayList<Coords>();
        max_x = 0;
        max_y = 0;
    }

    public void addGalaxy(Coords c) {
        galaxies.add(c);
        if (c.getY() > max_y)
            max_y = c.getY();
        if (c.getX() > max_x)
            max_x = c.getX();
    }

    public List<Coords> getGalaxies() {
        return galaxies;
    }



    public List<Coords> emptySpace() {
        boolean check;

        List<Coords> empty_space = new ArrayList<Coords>();
        
        for (int y = 0; y <= max_y; y++) {
            check = true;
            for (Coords g: galaxies) 
                if (g.getY() == y)
                    check = false;
            if (check)
                empty_space.add(new Coords(-1, y));
        }
        for (int x = 0; x <= max_x; x++) {
            check = true;
            for (Coords g: galaxies) 
                if (g.getX() == x)
                    check = false;
            if (check)
                empty_space.add(new Coords(x, -1));
        }

        return empty_space;
    }
}
