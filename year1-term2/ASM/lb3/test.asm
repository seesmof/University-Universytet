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
    
    lea dx, new_line
    call outputString

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

    lea dx, new_line
    call outputString

    lea dx, new_line
    call outputString
    lea dx, horizontal_line
    call outputString
    lea dx, new_line
    call outputString
    lea dx, my_string
    call outputString
    lea dx, new_line
    call outputString
    lea dx, student_group
    call outputString
    lea dx, new_line
    call outputString
    lea dx, new_line
    call outputString
    lea dx, current_year
    call outputString
    lea dx, new_line
    call outputString
    lea dx, horizontal_line
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
    ; Define a new line character and initialize it
    new_line db 0Dh, 0Ah, '$'

    ; Define a byte and initialize it with a value
    my_byte db 10h

    ; Define a word and initialize it with a value
    my_word dw 1234h

    ; Define a dword and initialize it with a value
    my_dword dd 5678h

    ; Define necessary string  and initialize them with corresponding values
    my_string db '      Oleh Onyshchenko', '$'
    student_group db '          KHT-122', '$'
    horizontal_line db '-------------------------------', '$'
    current_year db '           2023', '$'

    ; Define an array of bytes and initialize it with values
    my_array db 1, 2, 3, 4, 5

    ; Define an array of words and initialize it with values
    my_matrix dw 1, 2, 3, 4, 5

    ; Define a 2-dimensional array of doublewords and initialize it with values
    myDwordArray dd 1, 2, 3, 4
                dd 5, 6, 7, 8
                dd 9, 10, 11, 12
dseg ends   ; end data segment

end start   ; end program execution