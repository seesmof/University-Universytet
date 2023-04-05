.model small    ; set program model as small
.stack 100h     ; set stack size to 100h

sseg segment para stack 'stack'     ; declare stack segment
    db 256 dup(?)       ; reserve memory for stack
sseg ends   ; end stack segment 

dseg segment para public 'data'     ; declare data segment
    section_one db '  1. Student Card:', '$'
    student_name db '      Onyshchenko Oleh', '$'
    student_group db '          KHT-122', '$'
    new_line db 0Dh, 0Ah, '$'
    current_year db '            2023', '$'
    verical_line db '-----------------------------', '$'

    section_two db '  2. Data Types:', '$'
    section_two_byte db '    2.1 Byte: ', '$'
    example_byte db 10
    section_two_word db '    2.2 Word: ', '$'
    example_word dw 1000
    section_two_dword db '    2.3 Double Word: ', '$'
    example_dword dd 12345678h
    section_two_float db '    2.4 Float: ', '$'
    example_float dd 3.14
    section_two_string db '    2.3 String: ', '$'
    example_string db 'Hello, Assembly', '$'
dseg ends   ; end data segment

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

    ; section one start
    lea dx, new_line
    call outputString

    lea dx, section_one
    call outputString
    lea dx, new_line
    call outputString

    lea dx, verical_line
    call outputString
    lea dx, new_line
    call outputString

    lea dx, student_name
    call outputString
    lea dx, new_line
    call outputString

    lea dx, student_group
    call outputString
    lea dx, new_line
    call outputString

    lea dx, new_line
    call outputString
    lea dx, new_line
    call outputString

    lea dx, current_year
    call outputString
    lea dx, new_line
    call outputString

    lea dx, verical_line
    call outputString
    lea dx, new_line
    call outputString
    
    lea dx, new_line
    call outputString
    ; section one end

    ; section two start
    lea dx, new_line
    call outputString

    lea dx, section_two
    call outputString
    lea dx, new_line
    call outputString

    lea dx, 

    lea dx, new_line
    call outputString
    ; section two end

    ret     ; stop function execution
main endp   ; end main function

outputString proc near
    sub ax, ax
    mov ah, 09h
    int 21h
    ret
outputString endp

cseg ends   ; end code segment
end start   ; end program execution