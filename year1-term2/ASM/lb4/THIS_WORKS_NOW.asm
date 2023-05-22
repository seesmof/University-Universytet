.model small
.stack 100h

.data
    intro db 0dh, 0ah, "        Onyshchenko Oleh", 0dh, 0ah, "$"
    group_name db "             KHT-122", 0dh, 0ah, "$"
    line db "-----------------------------------", 0dh, 0ah, "$"
    msg1 db 0dh, 0ah, "Enter the first number: $"
    msg2 db 0dh, 0ah, "Enter the second number: $"
    result_dec db 0dh, 0ah, "Result in decimal: $"
    result_bin db 0dh, 0ah, "Result in binary: $"
    buffer db 9 dup ('$') 
    endl db 0dh, 0ah, "$"

.code
.startup
    mov ax, @data
    mov ds, ax

    mov ah, 09h
    lea dx, intro
    int 21h
    lea dx, group_name
    int 21h
    lea dx, line
    int 21h

    mov ah, 09h
    lea dx, msg1
    int 21h

    mov ah, 01h
    int 21h
    sub al, '0'
    mov bl, al

    mov ah, 09h
    lea dx, msg2
    int 21h

    mov ah, 01h
    int 21h
    sub al, '0'
    mov cl, al

    add bl, cl

    mov ah, 09h
    lea dx, result_dec
    int 21h
    mov dl, bl 
    add dl, '0' 
    mov ah, 02h 
    int 21h 

    mov ch, 8
    mov si, offset buffer
    mov cl, bl

convert_loop:
        mov al, cl
        and al, 10000000b
        shr al, 7
        or al, 00110000b
        mov [si], al
        inc si
        shl cl, 1
        dec ch
        jnz convert_loop

    mov ah, 09h
    lea dx, result_bin
    int 21h

    mov dx, offset buffer
    mov ah, 09h
    int 21h
    lea dx, endl
    int 21h

    mov ah, 09h
    lea dx, endl
    int 21h
    lea dx, line
    int 21h

    mov ah, 4ch
    int 21h

.exit
end
