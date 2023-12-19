package day14;

import java.util.ArrayList;
import java.util.List;

public class Main {


    public static int getTotal(Platform platform) {
        int total = 0;
        for (Rock r: platform.getRocks()) {
            if (r.isMovable())
                total += platform.getColumnLength() + 1 - r.getY();
        }
        return total;
    }

    public static void part1(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  

        Platform platform = reader.getPlatform();
        platform.tilt('N');
        
        System.out.println(getTotal(platform));


    }

    public static void part2(String file_name) throws Exception {
        Reader reader = new Reader(file_name);  
        int cycles = 1000000000;
        

        Platform platform = reader.getPlatform();
        List<Platform> last_platforms = new ArrayList<Platform>();

        int inner_cycle = -1;
        int last_cycles = 0;
        
        for (int c=0; c < cycles; c++) {
            platform.spin();
            for (Platform last : last_platforms)
                if (platform.equals(last)) {
                    inner_cycle = c- last_platforms.indexOf(last);
                    break;
            }
            if (inner_cycle != -1) {
                last_cycles = (cycles-c-1)%inner_cycle;
                break;
            }
            last_platforms.add(platform.clone());
        }

        for (int c=0; c < last_cycles; c++) {
            platform.spin();
        }

        System.out.println(getTotal(platform));
    }

    public static void main(String[] args) throws Exception {

        String file_name = "day14/day14_input.txt";

        try {
            part1(file_name);
        } catch (Exception e) {
            System.err.println("Part 1 Failed " + e);
        }
        try {
            part2(file_name);
        } catch (Exception e) {
            System.err.println("Part 2 Failed " + e);
        }

    }   
}
