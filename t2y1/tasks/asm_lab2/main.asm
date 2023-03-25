.model small         ; Defines the memory model of the program (in this case, small)
.stack 100h          ; Sets the size of the program stack to 256 bytes (100h in hexadecimal)

sseg segment para stack 'stack' ; Declares the stack segment
    db 256 dup(?)               ; Reserves 256 bytes of memory for the stack
sseg ends                       ; Ends the stack segment declaration

dseg segment para public 'data' ; Declares the data segment as a public segment
    symbol db 'X'               ; Declares a byte variable named 'symbol' with the value of 'X'
dseg ends                       ; Ends the data segment declaration

cseg segment para public 'code'         ; Declares the code segment as a public segment
    assume cs:cseg, ss:sseg, es:nothing ; Sets the segment registers for the code segment (CS), stack segment (SS), and extra segment (ES) to the current segment (cseg), stack segment (sseg), and nothing, respectively

start:                 ; Marks the entry point of the program

    assume ds:dseg     ; Sets the data segment register (DS) to the value of the data segment (dseg)
    mov bx, dseg       ; Copies the value of dseg to the BX register
    mov ds, bx         ; Sets the data segment register (DS) to the value in the BX register

    call main          ; Calls the main procedure

    mov ah, 4Ch        ; Sets the value of AH to 4C (exit program to operating system)
    mov bl, 6Ch        ; Sets the value of BL to 108 (return code of 108, meaning execution with an error)
    int 21h            ; Performs software interrupt to terminate the program

main proc near         ; Declares the main procedure
    mov dl, symbol     ; Loads the value of 'symbol' into the DL register (which represents a character to output)
    mov ah, 02h        ; Sets the value of AH to 02h (select function to output character to console)
    int 21h            ; Performs software interrupt to output character to console

    ret                ; Returns from the main procedure
main endp              ; Ends the main procedure

cseg ends              ; Ends the code segment
end start              ; Ends the program
