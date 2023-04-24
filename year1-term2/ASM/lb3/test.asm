.model small    ; set program model as small
.stack 100h     ; set stack size to 100h

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
    lea dx, new_line
    call outputString

    mov dl, my_byte
    add dl, '$'
    call outputSymbol
    lea dx, new_line
    call outputString

    lea dx, my_string
    call outputString
    lea dx, new_line
    call outputString

    ret
main endp   ; end main function

outputString proc near
    sub ax, ax
    mov ah, 09h
    int 21h
    ret
outputString endp

outputSymbol proc near
    sub ax, ax
    mov ah, 02h
    int 21h
    ret
outputSymbol endp
cseg ends   ; end code segment

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

dseg segment para public 'data'     ; declare data segment
    new_line db 0Dh, 0Ah, '$'

    ; Define variables of different types and sizes
    my_byte db 10h
    my_word dw 1234h
    my_dword dd 5678h
    my_string db 'Oleh Onyshchenko KHT-122', 0
    my_array db 1, 2, 3, 4, 5
    my_matrix dw 1, 2, 3, 4, 5, 6, 7, 8, 9
dseg ends   ; end data segment

end start   ; end program execution