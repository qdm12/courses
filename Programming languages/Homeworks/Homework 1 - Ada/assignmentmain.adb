with Ada.Text_IO, Ada.Integer_Text_io, matrixmult;

use matrixmult; -- MatMult, SIZE and Matrix_Type

procedure AssignmentMain is
    A, B, C : Matrix_Type;
    
    -- Reader2: Reads the second matrix from standard input
    -- It is called by Reader1 when Reader1 is done
    task Reader2 is
        entry start;
    end Reader2;
    task body Reader2 is
    begin
        accept start do
            for row in 1 .. SIZE loop
                for col in 1 .. SIZE loop
                    Ada.Integer_Text_io.get(B(row, col));
                end loop;
            end loop;
        end start;
    end Reader2;
    
    -- Reader1: Reads the first matrix from standard input
    -- This task starts directly at the start of the program
    task Reader1 is
        entry start;
    end Reader1;
    task body Reader1 is
    begin
        accept start do
            for row in 1 .. SIZE loop
                for col in 1 .. SIZE loop
                    Ada.Integer_Text_io.get(A(row, col));
                end loop;
            end loop;
            Reader2.start; -- Reads the second matrix
        end start;
    end Reader1;
    
    procedure ReadMatrices is
    begin
        Reader1.start;
    end;
    
    task Printer is
        entry print;
    end Printer;
    task body Printer is
    begin
        accept print do
            for row in 1 .. SIZE loop
                for col in 1 .. SIZE loop
                    Ada.Text_IO.Put(Integer'Image(C(row,col)));
                end loop;
                Ada.Text_IO.New_Line;
            end loop;
        end print;
    end Printer;
begin
    ReadMatrices; -- to block until A and B are fully read
    MatMult(A, B, C);    
    Printer.print; 
end AssignmentMain;