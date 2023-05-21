.model small
.stack 100h

.data
num1 db 6 ; maximum number of digits to read for num1
num2 db 6 ; maximum number of digits to read for num2
buf1 db 6 dup('?') ; buffer to store num1 string
buf2 db 6 dup('?') ; buffer to store num2 string
result dw ? 

.code
start:
mov ax, @data
mov ds, ax

; Prompt user to enter first number
mov ah, 9
mov dx, offset msg_num1
int 21h

; Read first number from user input
mov ah, 0Ah
mov dx, offset buf1
int 21h

; Convert string to number
call parse_num1

; Prompt user to enter second number
mov ah, 9
mov dx, offset msg_num2
int 21h

; Read second number from user input
mov ah, 0Ah
mov dx, offset buf2
int 21h

; Convert string to number
call parse_num2

; Add the numbers and store result in 'result' variable
mov ax, num1
add ax, num2
mov result, ax

; Convert result to binary using 16-bit registers
mov bx, 0
mov cx, 16

loop1:
rol ax, 1
adc bh, 0
loop loop1

; Print the binary result to console
mov ah, 9
mov dx, offset msg_result
int 21h

mov cx, 16

loop2:
shr bh, 1
rcr result, 1
mov dl, '0'
adc dl, 0
mov ah, 2
int 21h
loop loop2

mov ah, 4ch
int 21h

parse_num1:
mov si, offset buf1
mov cl, [si] ; first character in buffer is count of digits
inc si ; move to start of actual digits
mov al, 0 ; clear out register
loop1:
mov bl, [si] ; current character
inc si ; move to next character
cmp bl, 0x0d ; check for carriage return
je done1
sub bl, '0' ; convert from ASCII to number
mul byte ptr [num10] ; multiply current number by 10
add al, bl ; add to current number
jmp loop1
done1:
mov num1, ax ; store converted number
ret

; Subroutine to convert string buffer to number
parse_num2:
mov si, offset buf2
mov cl, [si] ; first character in buffer is count of digits
inc si ; move to start of actual digits
mov al, 0 ; clear out register
loop2:
mov bl, [si] ; current character
inc si ; move to next character
cmp bl, 0x0d ; check for carriage return
je done2
sub bl, '0' ; convert from ASCII to number
mul byte ptr [num10] ; multiply current number by 10
add al, bl ; add to current number
jmp loop2
done2:
mov num2, ax ; store converted number
ret

msg_num1 db 'Enter the first number: $'
msg_num2 db 'Enter the second number: $'
msg_result db 'The binary result is: $'
num10 db 10 ; used for converting ASCII to number
end start
