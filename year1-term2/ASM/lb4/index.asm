.model small
.stack

.data
    num1 db ?
    num2 db ?
    operator db ?
    result db ?
    msg1 db 'Enter the first number: $'
    msg2 db 'Enter the second number: $'
    msg3 db 'Enter the operator (+ - * /): $'
    msg4 db 'Result: $'
    endl db 0Dh, 0Ah, '$'

.code
main proc
    mov ax, @data
    mov ds, ax

    ; Prompt user for first number
    mov ah, 09h
    lea dx, msg1
    int 21h

    ; Read first number
    mov ah, 01h
    int 21h
    sub al, 30h ; Convert ASCII to binary
    mov num1, al
    mov ah, 09h
    lea dx, endl
    int 21h

    ; Prompt user for second number
    mov ah, 09h
    lea dx, msg2
    int 21h

    ; Read second number
    mov ah, 01h
    int 21h
    sub al, 30h ; Convert ASCII to binary
    mov num2, al
    mov ah, 09h
    lea dx, endl
    int 21h

    ; Prompt user for operator
    mov ah, 09h
    lea dx, msg3
    int 21h

    ; Read operator
    mov ah, 01h
    int 21h
    mov operator, al
    mov ah, 09h
    lea dx, endl
    int 21h

    ; Perform arithmetic operation based on operator
    cmp operator, '+'
    je add_numbers
    cmp operator, '-'
    je subtract_numbers
    cmp operator, '*'
    je multiply_numbers
    cmp operator, '/'
    je divide_numbers

    add_numbers:
        mov al, num1
        add al, num2
        mov result, al
        jmp display_result

    subtract_numbers:
        mov al, num1
        sub al, num2
        mov result, al
        jmp display_result

    multiply_numbers:
        mov al, num1
        mul num2
        mov result, al
        jmp display_result

    divide_numbers:
        mov al, num1
        mov bl, num2
        div bl
        mov result, al
        jmp display_result

    display_result:
        ; Display result
        mov ah, 09h
        lea dx, endl
        int 21h
        mov ah, 09h
        lea dx, msg4
        int 21h

        mov al, result
        add al, 30h ; Convert binary to ASCII
        mov dl, al
        mov ah, 02h
        int 21h

        mov ah, 4ch ; Exit program
        int 21h
main endp
end main
