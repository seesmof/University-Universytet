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
    ; output new line
    lea dx, new_line
    call outputString

    ; output a byte character
    mov dl, my_byte
    ; use null terminator to output the character itself
    add dl, '$'
    call outputSymbol
    ; output new line
    lea dx, new_line
    call outputString

    ; output new line
    lea dx, new_line
    call outputString

    ; Initialize counter to 5
    mov cx, 5
    ; Initialize pointer to my_array
    mov si, offset my_array

    ; Loop 5 times
    loop_start:
        ; Load byte at memory address pointed to by si into dl
        mov dl, [si]
        ; Add ASCII value of $ to dl
        add dl, '$'
        ; Output resulting character to console
        call outputSymbol
        ; Load memory address of _space string into dx
        lea dx, _space
        ; Output space character to console
        call outputString

        ; Increment pointer to point to next byte in array
        inc si
        ; Repeat loop until cx reaches 0
        loop loop_start

    ; output new line
    lea dx, new_line
    call outputString

    ; initialize CX register with the number of characters in the message string
    mov cx, 8
    ; initialize SI register with the offset of the message string
    mov si, offset message

    ; Loop through each character in the message string and print it
    print_message:
        mov dl, [si]     ; load the current character into DL register
        call outputSymbol   ; print the character in DL register
        lea dx, _space   ; load the offset of the space character into DX register
        call outputString   ; print the space character
        inc si           ; move to the next character in the message string
        loop print_message  ; repeat until all characters have been printed

    ; output new line
    lea dx, new_line
    call outputString

    ; output new line
    lea dx, new_line
    call outputString
    lea dx, horizontal_line
    call outputString
    ; output new line
    lea dx, new_line
    call outputString
    lea dx, my_string
    call outputString
    ; output new line
    lea dx, new_line
    call outputString
    lea dx, student_group
    call outputString
    ; output new line
    lea dx, new_line
    call outputString
    ; output new line
    lea dx, new_line
    call outputString
    lea dx, current_year
    call outputString
    ; output new line
    lea dx, new_line
    call outputString
    lea dx, horizontal_line
    call outputString
    ; output new line
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
    ; Define a space character and initialize it
    _space db ' ', '$'

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
    message db 'Assembly', '$'

    ; Define an array of bytes and initialize it with values
    my_array db 1, 2, 3, 4, 5

    ; Define an array of words and initialize it with values
    my_matrix dw 1, 2, 3, 4, 5

    ; Define a 2-dimensional array of doublewords and initialize it with values
    my_dword_matrix dd 1, 2, 3, 4
                dd 5, 6, 7, 8
                dd 9, 10, 11, 12
dseg ends   ; end data segment

end start   ; end program execution