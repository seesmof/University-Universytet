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
    mov ax, @data
    mov ds, ax

    ; Output a byte variable
    mov dl, my_byte
    add dl, '0'
    mov ah, 2
    int 21h

    ; Output a word variable
    mov ax, my_word
    mov bh, 0
    mov bl, 10
    div bl
    add ax, '0'
    mov dl, al
    mov ah, 2
    int 21h
    mov dl, ah
    add dl, '0'
    mov ah, 2
    int 21h

    ; Output a dword variable
    mov eax, my_dword
    mov bh, 0
    mov bl, 10
    div bl
    add ax, '0'
    mov dl, al
    mov ah, 2
    int 21h
    mov dl, ah
    add dl, '0'
    mov ah, 2
    int 21h
    mov eax, my_dword
    shr eax, 16
    mov bh, 0
    mov bl, 10
    div bl
    add ax, '0'
    mov dl, al
    mov ah, 2
    int 21h
    mov dl, ah
    add dl, '0'
    mov ah, 2
    int 21h

    ; Output a string variable
    mov dx, offset my_string
    mov ah, 9
    int 21h

    ; Output an array variable
    mov cx, 5
    mov si, offset my_array
    loop_start:
        mov dl, [si]
        add dl, '0'
        mov ah, 2
        int 21h
        inc si
        loop loop_start

    ; Output a matrix variable
    mov cx, 3
    mov si, offset my_matrix
    loop_row:
        mov bx, cx
        mov dx, offset my_matrix
        add dx, bx
        mov dl, [si]
        add dl, '0'
        mov ah, 2
        int 21h
        inc si
        loop loop_row

    mov ah, 4ch
    int 21h
main endp   ; end main function

outputString proc near
    sub ax, ax
    mov ah, 09h
    int 21h
    ret
outputString endp
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
    my_string db 'Hello, world!', 0
    my_array db 1, 2, 3, 4, 5
    my_matrix dw 1, 2, 3, 4, 5, 6, 7, 8, 9
dseg ends   ; end data segment

end start   ; end program execution