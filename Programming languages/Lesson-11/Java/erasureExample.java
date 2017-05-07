/* Erasure property of generics (run-time representations of all instances 
   of one generic is the same). The type parameter information is only
   used at compile time. */
import java.util.*;

public class erasureExample{
    public static void main(String args[]) {
        ArrayList<Integer> li = new ArrayList<Integer>();
        ArrayList<Float> lf = new ArrayList<Float>();        
        System.out.println(li.getClass().toString());
        System.out.println(lf.getClass().toString());
        // Both print class java.util.ArrayList
        if (li.getClass() == lf.getClass()){ // true
            System.out.println("Equal");
        }
    }
}