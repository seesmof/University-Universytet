.model small
.stack 100h

.data
    msg db 'Enter a number: $'
    num db 10, ? ; max length of input is 10 characters
    base db 10 ; default number system is decimal
    NUM1 db ?

.code
main proc
    mov ax, @data
    mov ds, ax

    ; display message
    mov ah, 9
    lea dx, msg
    int 21h

    ; read input string
    mov ah, 0Ah
    lea dx, num
    int 21h

    ; convert input string to number
    xor ax, ax ; clear ax
    xor bx, bx ; clear bx
    mov bl, base ; set base
    mov si, offset num+2 ; set si to start of input string
    mov cl, [num+1] ; set cl to length of input string
convert_loop:
    cmp cl, 0 ; check if end of input string
    je convert_done
    mov dl, [si] ; get current digit
    cmp dl, '0' ; check if digit is less than '0'
    jb convert_error
    cmp dl, '9' ; check if digit is greater than '9'
    ja check_alpha
    sub dl, '0' ; convert digit to value
    jmp convert_continue
check_alpha:
    cmp dl, 'A' ; check if digit is less than 'A'
    jb convert_error
    cmp dl, 'Z' ; check if digit is greater than 'Z'
    ja convert_error
    sub dl, 'A' - 10 ; convert digit to value
    jmp convert_continue
convert_error:
    ; handle error
    int 21h
    jmp convert_done
convert_continue:
    ; update ax with new digit
    mul bl ; ax = ax * base
    add ax, dx ; ax = ax + dl
    inc si ; move to next digit
    dec cl ; decrement length
    jmp convert_loop
convert_done:
    ; ax now contains the converted number
    ; display result
    mov num1, ax
    mov ah, 9
    lea dx, num1
    int 21h

    mov ah, 4Ch
    int 21h
main endp

end main
