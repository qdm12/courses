/* Use of bounds for the type parameters to generic classes & methods. */
import java.util.List;
import java.util.ArrayList;
import java.util.Vector;

class A {public int x = 4;}
class B extends A {public int y = 7;}
public class bounded {
    static <T extends A> List<T> id(List<T> l){return l;}
    static <E> void insert(List<E> l, E elt){l.add(elt);}
    static void insertB(List<? super B> l, B elt){l.add(elt);}
    static <E extends A> void insertListA(List<A> l, E elt){l.add(elt);}
    public static void main(String[] args){
        A a = new A();
        B b = new B();
        List<A> la = new ArrayList<A>();
        List<B> lb = new ArrayList<B>();
        insert(la,a);
        insert(la,b);
        insert(lb,a); // ERROR
        insert(lb,b);
        la = id(la);
        lb = id(lb);	
    }
}