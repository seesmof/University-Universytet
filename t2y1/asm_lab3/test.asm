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
    edl     db 0Dh, 0Ah, '$'
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

m0:
    lea dx,h    ; text to output
    call outputStirng   ; output with function
    lea dx,edl  ; new line to output
    call outputStirng   ; output with function
    loop m0

    ret     ; stop function execution
main endp   ; end main function

outputStirng proc near
    sub ax,ax
    mov ah,09h
    int 21h
    ret
outputStirng endp

cseg ends   ; end code segment
end start   ; end program execution