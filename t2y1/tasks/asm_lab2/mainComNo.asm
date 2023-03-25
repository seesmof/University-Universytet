.model tiny     ; set program model as tiny

cseg segment para public 'code'     ; Declare code segment
    assume cs:cseg, ds:cseg, ss:cseg, es:nothing    ; set each code segment to code seg as it is the only segment in the program 
    org 100h    ; start loading the first instruction at 100h

start:  ; declare program entry point
    call main   ; call main function

    mov ah, 04Ch    ; exit to OS
    mov bl, 6Ch     ; set error code to 108 in hex 
    int 21h     ; call interrupt
    
    symbol db 'U'   ; declare a symbol to output

main proc near  ; declare main procedure
    xor ax, ax   ; clear ax register
    mov dl, symbol      ; load symbol to stdout 
    mov ah, 02h     ; output symbol to stdout
    int 21h     ; call interrupt

    mov dl, 'k'
    mov ah, 02h
    int 21h

    mov dl, 'r'
    mov ah, 02h
    int 21h

    mov dl, 'a'
    mov ah, 02h
    int 21h

    mov dl, 'i'
    mov ah, 02h
    int 21h

    mov dl, 'n'
    mov ah, 02h
    int 21h

    mov dl, 'e'
    mov ah, 02h
    int 21h

    mov dl, 10
    mov ah, 02h
    int 21h
    mov dl, 13
    mov ah, 02h
    int 21h

    ret ; end function execution
main endp   ; end procedure

newLine proc near   ; declare modular procedure

cseg ends   ; close segment
end start   ; end program execution