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
    call outputString ; output with function

    lea dx, input_prompt
    call outputString ; output with function
    
    lea dx, input_buffer
    call inputString ; set output string

    sub bx, bx
    mov bl, buffer_length
    mov [buffer_cont + bx], '$'

    lea dx, new_line
    call outputString ; output with function

    lea dx, new_line
    call outputString ; output with function

    lea dx, output_prompt
    call outputString ; output with function

    lea dx, buffer_cont
    call outputString ; set output string
    lea dx, new_line
    call outputString ; output with function

    ret     ; stop function execution
main endp   ; end main function

inputString proc near
    sub ax, ax
    mov ah, 0Ah
    int 21h
    ret
inputString endp

outputString proc near
    sub ax, ax
    mov ah, 09h
    int 21h
    ret
outputString endp
cseg ends   ; end code segment

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

dseg segment para public 'data'     ; declare data segment
    new_line db 0Dh, 0Ah, '$'
    input_prompt db 'Enter a string: ', '$'
    output_prompt db 'Your string: ', '$'

    input_buffer db 100
    buffer_length db ?
    buffer_cont db 100 dup (' ')

    ; Define a byte variable and initialize it with a value
    myByte db 10

    ; Define a word variable and initialize it with a value
    myWord dw 1234h

    ; Define a doubleword variable and initialize it with a value
    myDword dd 12345678h

    ; Define a string variable and initialize it with a value
    myString db 'Hello, world!', 0

    ; Define an array of bytes and initialize it with values
    myByteArray db 1, 2, 3, 4, 5

    ; Define an array of words and initialize it with values
    myWordArray dw 1, 2, 3, 4, 5

    ; Define a 2-dimensional array of doublewords and initialize it with values
    myDwordArray dd 1, 2, 3, 4
                dd 5, 6, 7, 8
                dd 9, 10, 11, 12
dseg ends   ; end data segment

end start   ; end program execution