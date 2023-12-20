package day16;

public class Beam {
    
    private Coords pos;
    private Character dir;

    public Beam(Coords pos, Character dir) {
        this.pos = pos;
        this.dir = dir;
    }

    public Character getDir() {
        return dir;
    }

    public Coords getPos() {
        return pos;
    }

    @Override
    public String toString() {
        String print = "";
        print += pos;
        print += dir;
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

        Beam other = (Beam) obj;
        return this.dir == other.dir &&
               this.pos.equals(other.pos);
    }
}
