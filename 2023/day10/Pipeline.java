package day10;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Pipeline {

    private Map<Coords, Character> pipes;

    private Coords start;
    private Coords prev;
    private Coords curr;
    private List<Coords> dirs;
    

    private Coords mapper(char dir) {
        if (dir == '|') {
            if (curr.equals(prev.sum(0, 1))) 
                return curr.sum(0, 1);
            else if (curr.equals(prev.sum(0, -1))) 
                return curr.sum(0, -1);
        }
        else if (dir == '-') {
            if (curr.equals(prev.sum(1, 0))) 
                return curr.sum(1, 0);
            else if (curr.equals(prev.sum(-1, 0))) 
                return curr.sum(-1, 0);
        }
        else if (dir == 'L') {
            if (curr.equals(prev.sum(0, 1))) 
                return curr.sum(1, 0);
            else if (curr.equals(prev.sum(-1, 0))) 
                return curr.sum(0, -1);
        }
        else if (dir == 'J') {
            if (curr.equals(prev.sum(0, 1))) 
                return curr.sum(-1, 0);
            else if (curr.equals(prev.sum(1, 0))) 
                return curr.sum(0, -1);
        }
        else if (dir == '7') {
            if (curr.equals(prev.sum(0, -1))) 
                return curr.sum(-1, 0);
            else if (curr.equals(prev.sum(1, 0))) 
                return curr.sum(0, 1);
        }
        else if (dir == 'F') {
            if (curr.equals(prev.sum(0, -1))) 
                return curr.sum(1, 0);
            else if (curr.equals(prev.sum(-1, 0))) 
                return curr.sum(0, 1);
        }
        return null;
    }

    public Pipeline() {
        pipes = new HashMap<Coords, Character>();
        start = null;

        dirs = new ArrayList<Coords>();
        dirs.add(new Coords(-1, 0));
        dirs.add(new Coords(1, 0));
        dirs.add(new Coords(0, -1));
        dirs.add(new Coords(0, 1));
    }

    public void addPipe(Coords xy, Character c) {
        pipes.put(xy, c);
        if (c == 'S')
            start = xy;
    }

    public Character getPipe(Coords xy) {
        return pipes.get(xy); 
    }

    public List<Coords> findConnection() {
        if (start == null)
            return null;
        
        List<Coords> path = new LinkedList<Coords>();
        Coords tmp;
        for (Coords dir: dirs) {
            path.clear();
            curr = start.sum(dir);
            prev = start;
            path.add(curr);

            while (curr != null && !curr.equals(start)) {
                if (pipes.get(curr) != null)
                    tmp = mapper(pipes.get(curr));
                else
                    break;
                prev = curr;
                curr = tmp;
                path.add(curr);
            }
            if (curr == null)
                continue;
            if (curr.equals(start))
                return path;
        }
        

        System.err.println("Couldn't be found");
        return null;
    }

    @Override
    public String toString() {
        String print = "";
        for (Coords c: pipes.keySet()) {
            print += c + " " + pipes.get(c)+"\n";
        }
        return print;

    }
}
