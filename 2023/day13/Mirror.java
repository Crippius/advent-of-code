package day13;

public class Mirror {

    private Character[][] mirror;
    private int row_length;
    private int column_length;

    private int row_multiplier = 100;
    private int column_multiplier = 1;
    private int last;

    public Mirror(Character[][] mirror, int row_length, int column_length) {
        this.mirror = mirror;
        this.row_length = row_length;
        this.column_length = column_length;
        last = -1;
    }

    public int findReflection(boolean not_last) {

        boolean is_reflection = true;

        for (int x = 0; x < column_length-1; x++) {
            is_reflection = true;
            int refl = 0;
            while (x-refl >= 0 && x+1+refl<column_length) {
                for (int i = 0; i<row_length; i++) {
                    
                    if (mirror[x-refl][i] != mirror[x+1+refl][i]) {
                        is_reflection = false;
                        break;
                    }
                }
                if (!is_reflection)
                    break;
                refl++;
            } 
            if (is_reflection) {
                if (not_last) {
                    if (last == (row_multiplier * (x+1)))
                        continue;
                    last = row_multiplier * (x+1);
                    return last;
                }
                else 
                    return row_multiplier * (x+1);
            }
        }
        for (int y = 0; y < row_length-1; y++) {
            is_reflection = true;
            int refl = 0;
            while (y-refl >= 0 && y+1+refl<row_length) {
                for (int i = 0; i<column_length; i++) {
                    if (mirror[i][y-refl] != mirror[i][y+1+refl]) {
                        is_reflection = false;
                        break;
                    }
                }
                if (!is_reflection)
                    break;
                refl++;
            } 
            if (is_reflection) {
                if (not_last) {
                    if (last == (column_multiplier * (y+1)))
                        continue;
                    last = column_multiplier * (y+1);
                    return last;
                }
                else 
                    return column_multiplier * (y+1);
            }
        }

        System.out.println("problem");
        return -1;
    }

    public void fixError() {
        boolean is_reflection = true;
        int errors = 1;
        int err_x = 0;
        int err_y = 0;

        for (int x = 0; x < column_length-1; x++) {
            errors = 1;
            is_reflection = true;
            int refl = 0;
            while (x-refl >= 0 && x+1+refl<column_length) {
                for (int i = 0; i<row_length; i++) {
                    
                    if (mirror[x-refl][i] != mirror[x+1+refl][i]) {
                        if (errors == 1) {
                            err_x = i;
                            err_y = x-refl;
                        }
                        errors--;
                        if (errors < 0) {
                            is_reflection = false;
                            break;
                        }
                    }
                }
                if (!is_reflection)
                    break;
                refl++;
            } 
            if (is_reflection && errors == 0) {
                mirror[err_y][err_x] = mirror[err_y][err_x] == '#' ? '.' : '#';
                return ;
            }
        }

        for (int y = 0; y < row_length-1; y++) {
            errors = 1;
            is_reflection = true;
            int refl = 0;
            while (y-refl >= 0 && y+1+refl<row_length) {
                for (int i = 0; i<column_length; i++) {
                    if (mirror[i][y-refl] != mirror[i][y+1+refl]) {
                        if (errors == 1) {
                            err_x = y-refl;
                            err_y = i;
                        }
                        errors--;
                        if (errors < 0) {
                            is_reflection = false;
                            break;
                        }
                    }
                }
                if (!is_reflection)
                    break;
                refl++;
            } 
            if (is_reflection && errors == 0) {
                mirror[err_y][err_x] = mirror[err_y][err_x] == '#' ? '.' : '#';
                return ;
            }
        }

        System.out.println("problem");
        return ;   
    }


    @Override
    public String toString() {
        String print = "";
        for (Character[] row: mirror) {
            for (Character c: row)
                print += c;
            print+= "\n";
        }

        print += "Row Length: ";
        print += row_length;
        print += "\nColumn Length: ";
        print += column_length;
        print += "\n";
        return print;
    }
    
}
