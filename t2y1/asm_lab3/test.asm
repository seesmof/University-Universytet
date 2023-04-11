.model small    ; set program model as small
.stack 100h     ; set stack size to 100h

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

; set up the data segment
dseg segment para public 'data'     ; declare data segment
    ; create variables of different types and sizes
    var1 db 1 ; byte variable
    var2 dw 2 ; word variable
    var3 dd 3 ; double word variable

    ; initialize variables in different ways and with different values
    var4 db ? ; uninitialized byte variable
    var5 db 'A' ; initialized with character value
    var6 db "Hello" ; initialized with string value

    ; create character strings and arrays with 1/2/4-byte elements of different dimensions
    str1 db "Hello, World!", '$'
    arr1 db 1, 2, 3, 4, 5 ; one-dimensional byte array
    arr2 dw 1, 2, 3, 4, 5 ; one-dimensional word array
    arr3 dd 1, 2, 3, 4, 5 ; one-dimensional double word array
dseg ends   ; end data segment

cseg segment para public 'code'     ; declare code segment
    assume cs:cseg, ss:sseg, es:nothing ; set segment register to corresponding ones
start:
    ; implement the output of any printed character to the console using interrupt function 2
    mov dl, 'A' ; move character to dl register
    mov ah, 02h ; set ah register to function code for outputting character to console
    int 21h ; call interrupt

; rest of the code goes here

cseg ends   ; end code segment
end start   ; end program execution