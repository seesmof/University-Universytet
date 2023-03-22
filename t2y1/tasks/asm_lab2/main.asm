; Set up the data segment
data segment
    ; Define a string to hold the output
    output db 80 dup('$')
data ends

; Set up the code segment
code segment
    ; Set the data segment register
    assume cs:code, ds:data

start:
    ; Initialize the data segment register
    mov ax, data
    mov ds, ax

    ; Set the number of rows in the triangle
    mov cx, 5

    ; Loop through each row of the triangle
row_loop:
    ; Calculate the number of stars in this row (2 * row - 1)
    mov ax, cx
    add ax, ax
    dec ax

    ; Calculate the starting position for this row ((80 - stars) / 2)
    mov bx, 80
    sub bx, ax
    shr bx, 1

    ; Set up a pointer to the output string
    lea si, output

    ; Add spaces before the stars in this row
space_loop:
    mov byte ptr [si], ' '
    inc si
    dec bx
    jnz space_loop

    ; Add stars to this row
star_loop:
    mov byte ptr [si], '*'
    inc si
    dec ax
    jnz star_loop

row_end:
    ; Output this row of the triangle
    mov ah, 9h
    lea dx, output
    int 21h