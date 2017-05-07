/* Use of generics to enforce static type checking (no run-time checks) */
import java.util.*;

public class fixed {
    public static void main(String[] args) {
        List<Integer> li = new LinkedList<Integer>();
        li.add(new Integer(6)); 
        li.add(new Integer(7)); 
        Iterator<Integer> i = li.iterator();
        Integer x = i.next(); // Don't need cast here
        x =  i.next(); // Don't need cast here
        System.out.println(x); // print 7
    }
}