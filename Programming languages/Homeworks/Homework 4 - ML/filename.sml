Control.Print.printDepth := 100;
Control.Print.printLength := 100;

(* Author: Quentin McGaw, netID: qm301 *)


(* 1. Define a polymorphic linear-time procedure, reverse L, where L is of type ’a list, that
returns a list containing the same elements as L, but in reverse order. You can use the same
algorithm as shown in the Scheme lecture. You can also define your own helper function if
you like (as I did in Scheme). Remember that to be linear time, reverse should not use the
append operator, @.*)
fun reverse_helper [] acc = acc
  | reverse_helper (z::zs) acc = reverse_helper zs (z::acc)

fun reverse L = reverse_helper L [];

(* 2. If you defined a separate helper function outside of reverse, write a function new reverse L,
where L is of type ’a list, that also reverses L but does not require a helper function outside
of new reverse. Note that you can nest a helper function inside of new reverse using a let.
Your code should be no more than 5 lines.
If you did not need a helper function outside of your reverse function, above, then you can
skip this part. *)
fun new_reverse L = let
  fun reverse_helper [] acc = acc
    | reverse_helper (z::zs) acc = reverse_helper zs (z::acc)
  in reverse_helper L []
  end;

(* 3. Write a polymorphic function, reduce depth L, where L is of type ’a list list (i.e. each
element of the list L is an ’a list), that returns a list of type ’a list whose elements are
the elements of the elements of L. That is, the result is a list whose depth of nesting is one
less than L’s depth. *)
fun reduce_depth [] = []
  | reduce_depth (z::zs) = z @ (reduce_depth zs);
  
(* 4. In ML, a set of integers can be representing as a list of integers, as long as that list has
no duplicate elements and is interpreted as being unordered. For this problem, define the
following infix operators:
    elt (membership test), such that 2 elt [1,2,3] returns true and 2 elt [1,3,4] returns false
    ++ (set union), such that [3,1,2,4] ++ [4,5,6,3] returns [1,2,4,5,6,3] (in any order).
    ** (set intersection), such that [3,1,2,4] ** [4,5,6,3] returns [3,4] (in any order).
    -- (set difference), such that [3,1,2,4] -- [4,5,6,3] returns [1,2] (in any order). *)
infix elt;
fun x elt [] = false
  | x elt (z::zs) = if x = z then true else (x elt zs);

infix ++;
fun S1 ++ S2 = S1 @ S2;

infix **;
fun [] ** S2 = []
  | S1 ** [] = []
  | S1 ** S2 = if hd(S2) elt S1 then hd(S2) :: (S1 ** tl(S2)) else (S1 ** tl(S2));

infix --;
fun [] -- S2 = []
  | S1 -- [] = S1
  | S1 -- S2 = if hd(S1) elt S2 then (tl(S1) -- S2) else hd(S1) :: (tl(S1) -- S2);
  
(* 5. Define a tree datatype, tree, where a leaf has an integer label and an interior node has an
integer label and two child trees. *)
datatype tree = leaf of int | node of int * tree * tree;

(* 6. Define a tree datatype, tree, where a leaf has an integer label and an interior node has an
integer label and two child trees. *)
datatype 'a ptree = pleaf of 'a | pnode of 'a * 'a ptree * 'a ptree;

(* 7. Write a function interior T, where T is an ’a ptree, that returns a list of the labels at the
interior nodes of T. The order of the list should reflect an in-order traversal of the tree. *)
fun interior (pleaf x) = []
  | interior (pnode(x, left, right)) = (interior left) @ (x :: interior right);
  
(* 8. Define the function mapTree f T, where f is of type ’a -> ’b and T is an ’a ptree, that
returns a new tree of type ’b ptree. The new ptree should have the same structure as T,
but differ only in its labels. In particular, each label at a pleaf or pnode of the new ptree
results from applying f to the label of the corresponding pleaf or pnode of T, respectively. *)
fun mapTree f (pleaf x) = pleaf(f x)
  | mapTree f (pnode(x, left, right)) = pnode(f x, mapTree f left, mapTree f right);
  
(* 9. Define a function, lexLess (op <) L1 L2, where L1 and L2 are both of type ’a list and
< is of type ’a * ’a -> bool, that performs a lexicographic less than comparison using the
passed-in < operator. A lexicographic less than operation on lists is defined as follows
    - [] is less than any non-empty list.
    - (x::xs) is less than (y::ys) iff:
        -  x < y, or
        -  x = y and xs is lexicographically less than ys *)
fun lexLess (op <) L1 [] = false
  | lexLess (op <) [] L2 = true
  | lexLess (op <) (x::xs) (y::ys) = if x < y then true
                                     else if y < x then false
                                     (* x = y *)
                                     else (lexLess (op <) xs ys);
                                     
(* 10. Define a function ptreeLess (op <) T1 T2, where T1 and T2 are of type ’a ptree and < is
of type ’a * ’a -> bool, that returns true iff T1 is less than T2. For this assignment, the
less than operator on ptree’s is defined as follows: 
    - a pleaf is less than a pnode.
    - a pleaf with a label x is less than a pleaf with a label y iff x is less than y.
    - a pnode with a label x and subtrees l1 and r1 is less than a pnode with label y and
      subtrees l2 and r2 iff:
        - l1 is less than l2, or
        - l1 = l2 and x is less than y, or
        - l1 = l2 and x = y and r1 is less than r2 *)
fun ptreeLess (op <) (pleaf x) (pnode(y, left, right)) = true
  | ptreeLess (op <) (pnode(y, left, right)) (pleaf x) = false
  | ptreeLess (op <) (pleaf x) (pleaf y) = if x < y then true else false
  | ptreeLess (op <) (pnode(x, l1, r1)) (pnode(y, l2, r2)) = if (ptreeLess (op <) l1 l2) then true (* l1 < l2 *)
                                                             else if (ptreeLess (op <) l2 l1) then false (* l1 > l2 *)
                                                             (* l1 = l2 *)
                                                             else if x < y then true
                                                             else if y < x then false
                                                             (* x = y *)
                                                             else (ptreeLess (op <) r1 r2); (* l1=l2, x=y, r1<r2 *)