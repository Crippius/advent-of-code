package day16;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Cave {
    
    private Map<Coords, Character> mirrors;
    private int column_length;
    private int row_length;
    private Map<Character, Coords> dirs;


    public Cave(Map<Coords, Character> mirrors, int row_length, int column_length) {
        this.mirrors = mirrors;
        this.column_length = column_length;
        this.row_length = row_length;

        dirs = new HashMap<Character, Coords>();
        dirs.put('N', new Coords(0, -1));
        dirs.put('W', new Coords(-1, 0));
        dirs.put('S', new Coords(0, +1));
        dirs.put('E', new Coords(+1, 0));
    }

    public int getColumnLength() {
        return column_length;
    }

    public int getRowLength() {
        return row_length;
    }



    private List<Beam> getBeams(Coords pos, Character dir, Character mirror) {

        List<Beam> next_beams = new ArrayList<Beam>();
        
        if (mirror == '.')
            next_beams.add(new Beam(pos, dir));
        else if (mirror == '/') {
            if (dir == 'N')
                next_beams.add(new Beam(pos, 'E'));
            if (dir == 'W')
                next_beams.add(new Beam(pos, 'S'));
            if (dir == 'S')
                next_beams.add(new Beam(pos, 'W'));
            if (dir == 'E')
                next_beams.add(new Beam(pos, 'N'));
        }
        else if (mirror == '\\') {
            if (dir == 'N')
                next_beams.add(new Beam(pos, 'W'));
            if (dir == 'W')
                next_beams.add(new Beam(pos, 'N'));
            if (dir == 'S')
                next_beams.add(new Beam(pos, 'E'));
            if (dir == 'E')
                next_beams.add(new Beam(pos, 'S'));
        }
        else if (mirror == '|') {
            if (dir == 'W' || dir == 'E') {
                next_beams.add(new Beam(pos, 'N'));
                next_beams.add(new Beam(pos, 'S'));
            }
            else
                next_beams.add(new Beam(pos, dir));
        }
        else if (mirror == '-') {
            if (dir == 'N' || dir == 'S') {
                next_beams.add(new Beam(pos, 'W'));
                next_beams.add(new Beam(pos, 'E'));
            }
            else
                next_beams.add(new Beam(pos, dir));
        }
        else
            System.err.println("problemi problemi");
        
        return next_beams;

    }

    private boolean inside(Coords pos) {
        return 0 <= pos.getX() && pos.getX() <= row_length &&
               0 <= pos.getY() && pos.getY() <= column_length; 
    }

    public int getTotalEnergizedTiles(Coords start, Character dir) {

        List<Beam> energized = new ArrayList<Beam>(); 
        List<Beam> curr = new ArrayList<Beam>();
        List<Beam> next = new ArrayList<Beam>();
        
        for (Beam b: getBeams(start, dir,  mirrors.containsKey(start) ? mirrors.get(start) : '.')) {
            curr.add(b);
            energized.add(new Beam(b.getPos(), b.getDir()));
        }

        int prev_size = -1;
        Character mirror;
        Coords new_coords;
    
        while (energized.size() != prev_size) {
            prev_size = energized.size();
            
            for (Beam beam: curr) {
                new_coords = beam.getPos().sum(dirs.get(beam.getDir()));
                if (!inside(new_coords))
                    continue;

                mirror = mirrors.containsKey(new_coords) ? mirrors.get(new_coords) : '.';

                for (Beam new_beam: getBeams(new_coords, beam.getDir(), mirror)) 
                    if (!energized.contains(new_beam)) {
                        next.add(new_beam);
                        energized.add(new Beam(new_beam.getPos(), new_beam.getDir()));
                    }
            }
            curr.clear();
            for (Beam b: next)
                curr.add(b);
            next.clear();
        }

        List<Coords> counter = new ArrayList<Coords>();
        for (Beam beam: energized)
            if (!counter.contains(beam.getPos()))
                counter.add(beam.getPos());
    
        return counter.size();
    }

    @Override
    public String toString() {
        String print = "";
        Coords c = new Coords(0, 0);

        for (int y=0; y<=column_length; y++) {
            for (int x=0; x<=row_length; x++) {
                c.setXY(x, y);
                if (mirrors.keySet().contains(c))
                    print += mirrors.get(c);
                else
                    print += ".";

            }
            print += "\n";
        }
        print += "\n";
        
        return print;
    }
}
