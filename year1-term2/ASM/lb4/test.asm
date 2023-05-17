.model small
.stack 100h

.data
msg1 db 'Enter the first number: $'
msg2 db 'Enter the second number: $'
msg3 db 'Choose an operation: $'
msg4 db '1. Add $'
msg5 db '2. Subtract $'
msg6 db '3. Multiply $'
msg7 db '4. Divide $'
msg8 db '5. Exit $'
result db 'Result: $'
endl db 0Dh, 0Ah, '$'

.code
mov ax, @data
mov ds, ax

; Get the first number
mov ah, 9
lea dx, msg1
int 21h

mov ah, 1
int 21h
sub al, 30h ; Convert ASCII to integer
mov bl, al

mov ah, 9
lea dx, endl
int 21h

; Get the second number
mov ah, 9
lea dx, msg2
int 21h

mov ah, 1
int 21h
sub al, 30h ; Convert ASCII to integer
mov bh, al

mov ah, 9
lea dx, endl
int 21h
mov ah, 9
lea dx, endl
int 21h

; Display the menu and get the choice
mov ah, 9
lea dx, msg3
int 21h
mov ah, 9
lea dx, endl
int 21h

lea dx, msg4
int 21h
mov ah, 9
lea dx, endl
int 21h

lea dx, msg5
int 21h
mov ah, 9
lea dx, endl
int 21h

lea dx, msg6
int 21h
mov ah, 9
lea dx, endl
int 21h

lea dx, msg7
int 21h
mov ah, 9
lea dx, endl
int 21h

lea dx, msg8
int 21h
mov ah, 9
lea dx, endl
int 21h

mov ah, 1
int 21h
sub al, 30h ; Convert ASCII to integer
cmp al, 1
je add_numbers
cmp al, 2
je subtract_numbers
cmp al, 3
je multiply_numbers
cmp al, 4
je divide_numbers
cmp al, 5
je exit_program

add_numbers:
mov ax, bx
add ax, cx
jmp display_result

subtract_numbers:
mov ax, bx
sub ax, cx
jmp display_result

multiply_numbers:
mov ax, bx
mul cx
jmp display_result

divide_numbers:
mov ax, bx
xor dx, dx ; Clear the DX register
div cx
jmp display_result

exit_program:
mov ah, 4ch
int 21h

display_result:
; Convert the result to ASCII and display it
add ax, 30h
mov ah, 0eh
lea dx, result
int 21h

mov al, ah
add al, 30h
mov ah, 0eh
int 21h

output_string:
mov ah, 9
int 21h

; Terminate the program
mov ah, 4ch
int 21h
end