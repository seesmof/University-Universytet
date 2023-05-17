.model small
.stack 100h

.data
    num1 db ?
    num2 db ?
    result dw ?

.code
    mov ax, @data
    mov ds, ax

    ; prompt user to enter first number
    mov ah, 9h
    lea dx, prompt1
    int 21h

    ; read first number as string
    mov ah, 0ah
    lea dx, num1
    int 21h

    ; convert first number to integer
    mov al, num1[2]
    sub al, '0'
    mov bl, num1[1]
    sub bl, '0'
    mov cl, 10
    mul cl
    add al, bl
    mov num1, al

    ; prompt user to enter second number
    mov ah, 9h
    lea dx, prompt2
    int 21h

    ; read second number as string
    mov ah, 0ah
    lea dx, num2
    int 21h

    ; convert second number to integer
    mov al, num2[2]
    sub al, '0'
    mov bl, num2[1]
    sub bl, '0'
    mul cl
    add al, bl
    mov num2, al

    ; display menu of mathematical operations
    mov ah, 9h
    lea dx, menu
    int 21h

    ; prompt user to choose operation
    mov ah, 1h
    int 21h
    sub al, '0'

    ; perform chosen operation
    cmp al, 1
    je add_nums
    cmp al, 2
    je sub_nums
    cmp al, 3
    je mul_nums
    cmp al, 4
    je div_nums

add_nums:
    mov al, num1
    add al, num2
    mov result, ax
    jmp display_result

sub_nums:
    mov al, num1
    sub al, num2
    mov result, ax
    jmp display_result

mul_nums:
    mov al, num1
    mul num2
    mov result, ax
    jmp display_result

div_nums:
    mov al, num1
    xor ah, ah
    div num2
    mov result, ax

display_result:
    ; display result
    mov ah, 9h
    lea dx, result_msg
    int 21h
    mov ax, result
    call print_num
    jmp exit_prog

print_num proc near
    push ax
    push bx
    push cx
    push dx

    mov bx, 10
    mov cx, 0

print_loop:
    xor dx, dx
    div bx
    push dx
    inc cx
    cmp ax, 0
    jne print_loop

display_loop:
    pop dx
    add dl, '0'
    mov ah, 2h
    int 21h
    loop display_loop

    pop dx
    pop cx
    pop bx
    pop ax
    ret
print_num endp

exit_prog:
    mov ah, 4ch
    int 21h

prompt1 db 'Enter first number: $'
prompt2 db 'Enter second number: $'
menu db 'Choose operation:', 13, 10, '1. Add', 13, 10, '2. Subtract', 13, 10, '3. Multiply', 13, 10, '4. Divide', 13, 10, '$'
result_msg db 'Result: $'
    
end
