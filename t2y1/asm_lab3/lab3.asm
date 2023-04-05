.model small    ; set program model as small
.stack 100h     ; set stack size to 100h

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

dseg segment para public 'data'     ; declare data segment
    space db ' ', '$'
    student_name db '      Onyshchenko Oleh', '$'
    student_group db '          KHT-122', '$'
    new_line db 0Dh, 0Ah, '$'
    current_year db '            2023', '$'
    verical_line db '-----------------------------', '$'
dseg ends   ; end data segment

cseg segment para public 'code'     ; declare code segment
    assume cs:cseg, ss:sseg, es:nothing ; set segment register to corresponding ones

start:  ; declare program entry point
    assume ds:dseg  ; set data segment register
    mov bx, dseg    ; add data segment to bx register
    mov ds, bx  ; set ds register to bx register

    call main   ; call main function

    mov ah, 04Ch     ; exit to OS
    mov bl, 06Ch     ; set error code to 108 in hex
    int 21h     ; call interrupt

main proc near  ; declare main function
    lea dx, verical_line
    call outputString
    lea dx, new_line
    call outputString

    lea dx, student_name
    call outputString
    lea dx, new_line
    call outputString

    lea dx, student_group
    call outputString
    lea dx, new_line
    call outputString

    lea dx, new_line
    call outputString
    lea dx, new_line
    call outputString

    lea dx, current_year
    call outputString
    lea dx, new_line
    call outputString

    lea dx, verical_line
    call outputString
    lea dx, new_line
    call outputString

    ret     ; stop function execution
main endp   ; end main function

outputString proc near
    sub ax, ax
    mov ah, 09h
    int 21h
    ret
outputString endp

cseg ends   ; end code segment
end start   ; end program execution