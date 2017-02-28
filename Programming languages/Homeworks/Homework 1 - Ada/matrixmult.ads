package MatrixMult is
    SIZE:constant Integer := 10;
    type Matrix_Type is array (1..SIZE, 1..SIZE) of integer;
    procedure MatMult(A : in Matrix_Type; B : in Matrix_Type; C : out Matrix_Type);
end MatrixMult;