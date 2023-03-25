.model tiny     ; set program model as tiny

cseg segment para public 'code'     ; Declare code segment
    assume cs:cseg, ds:cseg, ss:cseg, es:nothing    ; set each code segment to code seg as it is the only segment in the program 
    org 100h    ; start loading the first instruction at 100h

start:  ; declare program entry point
    call main   ; call main function

    mov ah, 04Ch ; 4C - function name to quit to OS. Exit to the OS
    mov bl, 6Ch     ; Error code 
    int 21h     ; Interrupttion of DOS. A function set
    
    symbol db 'U'   ; Declare A symbol

main proc near   ; proc = like func. Here we declare a function or a procedure called main
    xor ax,ax   ; AX <- 0
    mov dl, symbol ; Symbol to stdout 
    mov ah,02h  
    int 21h

    ret ; End function execution and return to the place where it was called
main endp   ; End procedure or function

cseg ends   ; Close segment
end start   ; End program