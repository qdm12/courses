package body MatrixMult is
    procedure MatMult(A : in Matrix_Type; B : in Matrix_Type; C : out Matrix_Type) is
        task type MyTaskType is
            entry CELL(row: in integer; col: in integer);
        end MyTaskType;
        task body MyTaskType is
        begin
            accept CELL(row: in integer; col: in integer) do
                C(row,col) := 0;
                for k in 1 .. SIZE loop
                    C(row,col) := C(row,col) + A(row,k)*B(k,col);
                end loop;
            end CELL;
        end MyTaskType;
        type Tasks_array is array (1..SIZE, 1..SIZE) of MyTaskType;
        MyTasks:Tasks_array;
    begin
        for row in 1 .. SIZE loop
            for col in 1 .. SIZE loop
                MyTasks(row, col).CELL(row, col);
            end loop;
        end loop;
    end;
end MatrixMult;

