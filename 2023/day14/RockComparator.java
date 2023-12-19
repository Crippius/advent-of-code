package day14;

import java.util.Comparator;

public class RockComparator implements Comparator<Rock> {

    private Character direction;

    public RockComparator(Character direction) {
        this.direction = direction;
    }

    @Override
    public int compare(Rock r1, Rock r2) {
        switch (direction) {
            case 'N':
                return r1.getY() - r2.getY();
            case 'E':
                return r2.getX() - r1.getX();
            case 'W':
                return r1.getX() - r2.getX();
            case 'S':
                return r2.getY() - r1.getY();
            default:
                return Integer.MAX_VALUE;
        }
    }
}