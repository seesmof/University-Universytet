.model small
.stack 100h

.data
num1 db ?
num2 db ?
result db ?
operator db ?

.code
main proc
    mov ax, @data
    mov ds, ax

    ; take two numbers and an operator as input from the user
    mov ah, 01h ; read character from keyboard
    int 21h
    sub al, '0'
    mov num1, al

    mov ah, 01h ; read character from keyboard
    int 21h
    sub al, '0'
    mov num2, al

    mov ah, 01h ; read character from keyboard
    int 21h
    mov operator, al

    ; perform the corresponding arithmetic operation
    cmp operator, '+'
    je add_nums

    cmp operator, '-'
    je sub_nums

    cmp operator, '*'
    je mul_nums

    cmp operator, '/'
    je div_nums

    ; handle invalid operator
    mov ah, 09h ; display string
    lea dx, invalid_operator_msg
    int 21h
    jmp exit_program

add_nums:
    mov al, num1
    add al, num2
    mov result, al
    jmp display_result

sub_nums:
    mov al, num1
    sub al, num2
    mov result, al
    jmp display_result

mul_nums:
    mov al, num1
    mul num2
    mov result, al
    jmp display_result

div_nums:
    mov al, num1
    div num2
    mov result, al
    jmp display_result

display_result:
    ; output the result to the user
    add result, '0'
    mov ah, 02h ; display character
    mov dl, result
    int 21h

exit_program:
    mov ah, 4ch ; terminate program
    int 21h
main endp

invalid_operator_msg db "Invalid operator!", 0

end main
