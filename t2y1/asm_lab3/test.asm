comment @
    Онищенко Олег
    КНТ-122
@

.model small    ; set program model as small
.stack 100h     ; set stack size to 100h

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

dseg segment para public 'data'     ; declare data segment
    x       equ 100
    a       db 0
    b       dw ?
    c       db 'A'
    d       db 65
    e       db 041h
    f       dw 0, 1, 2, 3, 4, ?, ?, ?, ?, ?
    g       db 'N', 'e', 'x', 't'
    h       db 'Next', '$'
    endl    db 0Dh, 0Ah, '$'
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
    sub ax,ax      ; ax == 0
    mov ah,09h     ; output string to stdout
    mov dx,offset h ; offset to string
    int 21h ; call interrupt

    mov ah,09h
    mov dx,offset endl
    int 21h

    ret     ; stop function execution
main endp   ; end main function

cseg ends   ; end code segment
end start   ; end program execution