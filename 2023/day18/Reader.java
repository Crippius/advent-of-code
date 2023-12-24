package day18;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Reader {

    private final BufferedReader br;

    private static Coords[] dirs_coords = {new Coords(0, -1), new Coords(-1, 0), new Coords(0, +1), new Coords(+1, 0)};
    
    private static Character[] dirs = {'U', 'L', 'D', 'R'};

    private static Character[] color_dirs = {'3', '2', '1', '0'};


    public Reader(String file_name) throws FileNotFoundException {
        File file = new File(file_name);

        br = new BufferedReader(new FileReader(file));
    }

    private Coords getDir(Character dir) {
        for (int i=0; i<dirs.length; i++) {
            if (dir == dirs[i])
                return dirs_coords[i];
            if (dir == color_dirs[i])
                return dirs_coords[i];
        }
        return null;
    }

    public List<Coords> getDigPlan(boolean color) throws IOException {

        List<Coords> plan = new ArrayList<Coords>();

        String str;
        int times;
        Coords dir;
        Coords curr = new Coords(0, 0);
        while ((str = br.readLine()) != null) {
            if (!color) {
                dir = getDir(str.split(" ")[0].charAt(0));
                times = Integer.parseInt(str.split(" ")[1]);
            }
            else {
                dir = getDir(str.split(" ")[2].charAt(7));
                times = Integer.parseInt(str.split(" ")[2].substring(2, 7), 16);
            }
            curr = curr.sum(dir.getX()*times, dir.getY()*times);
            plan.add(curr);
            
        }
        

        return plan;
    }
}
