import java.util.Collection;
import java.util.ArrayList;

class A {
    int value = 0;
    A(int v){value = v;}
    void add1(){value++;}
    public String toString(){return "A:"+value;}
}
class B extends A {
    B(int v){super(v);} // super is compulsory to call A's constructor.
    public String toString(){return "B:"+value;}
}
class C extends B {
    C(int v){super(v);}
    public String toString(){return "C:"+value;}
}

class testGenerics {
    // Simple generic method to print a Collection<E>, for any type E.
    static <E> void printCollection(Collection<E> c){
        for (E e : c){System.out.print(e + " ");}
        System.out.println();
    }
    // Generic method to insert elements of one Collection<E> in another.
    static <E> void copyCollection(Collection<E> d, Collection<E> c){
        for(E e : c){d.add(e);}
    }
    // Non-generic method to call add1 on each value in a Collection<A>
    static void add1Collection(Collection<A> c){
        for(A e : c){e.add1();}
        }
    // Generic version of the previous method, for any subtype of A (or A).
    static <E extends A> void genericadd1Collection(Collection<E> c){
        for(E e : c){e.add1();}
    }
    /* Non-generic method to insert a new B object in a Collection<B>.
       Since there is no subtyping on Collections (or any other instances 
       of generic classes), addB can only be called on arguments of type Collection<B>. */
    static void addB(Collection<B> c){
        B b = new B(100);
        c.add(b);
    }
    /* Generic version of addB callable on a collection of any type 
       supertype of B (or B). */
    static void newaddB(Collection<? super B> c){
        B b = new B(100);
        c.add(b);
    }
    /* Inserts elements from a collection of any type subtype of B (or B) 
       into a collection of any type supertype of B (or B).
       Illustrates how covariance is safe for reading values from a collection 
       and how contravariance is safe for inserting values in a collection. */
    static void copyBCollection(Collection<? super B> d, Collection<? extends B> c){
        for(B e : c){d.add(e);}
    }
    /* Copies elements from one collection to another, in the least 
       restrictive (but type-safe) way possible. */
    static <T> void copyAnyCollection(Collection<T> d, Collection<? extends T> c){
        for(T t: c){d.add(t);}
    }
    /* This is equivalent to the one above. */
    static <T> void copyAnyCollection2(Collection<? super T> d, Collection<T> c){
        for(T t: c){d.add(t);}
    }

    public static void main(String args[]){
        ArrayList<Integer> ai = new ArrayList<Integer>();
        ArrayList<Integer> bi = new ArrayList<Integer>();
        for(int i = 0; i < 10; i++){
            ai.add(i);
        }
        printCollection(ai); //0 1 ... 9
        bi.add(-1); // bi = [-1]
        copyCollection(bi, ai); 
        printCollection(bi); // -1 0 1 2 3 4 ... 9
        Integer y = bi.get(2) + bi.get(4);
        System.out.println(y); // 1 + 3 = 4

        ArrayList<A> aA = new ArrayList<A>();
        ArrayList<B> aB = new ArrayList<B>();
        ArrayList<C> aC = new ArrayList<C>();
        for(int i = 0; i < 10; i++){
            aA.add(new A(i));
            aB.add(new B(i));
            aC.add(new C(i));
        }
        printCollection(aA); // A:0 A:1 ... A:9
        printCollection(aB); // B:0 B:1 ... B:9
        printCollection(aC); // C:0 C:1 ... C:9

        add1Collection(aA);
        printCollection(aA); // A:1 A:2 ... A:10

        //add1Collection(aB); // ERROR
        genericadd1Collection(aB);
        printCollection(aB); // B:1 B:2 ... B:10
    
        newaddB(aA);
        //newaddB(aC); //ERROR
        addB(aB);
        
        ArrayList<A> aaa = new ArrayList<A>();
        ArrayList<B> bbb = new ArrayList<B>();
        ArrayList<C> ccc = new ArrayList<C>();
        copyBCollection(aaa,aB);
        //copyBCollection(bbb,aA); // ERROR
        copyBCollection(bbb,aB);
        copyBCollection(bbb,aC);
        //copyBCollection(ccc,aB); // ERROR

        printCollection(aaa); // B:1 B:2 ... B:10 B:100
        printCollection(bbb); // B:1 ... B:10 B:100 C:0 C:1 ... C:9
        printCollection(ccc); // B:1 ... B:10
    }
}
