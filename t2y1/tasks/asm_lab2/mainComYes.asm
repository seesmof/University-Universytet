.model tiny

.data
    char db 'G'    ; define a character to display

.code
DISP PROC
    mov ah, 02h    ; set the print service number
    mov dl, char   ; set the character to display
    int 21h        ; call the DOS service to display the character
    ret            ; return from the procedure
DISP ENDP

MAIN PROC
    call DISP     ; call the procedure to display the character
    mov ah, 4Ch   ; set the exit service number
    mov al, 108   ; set the return code
    int 21h       ; call the DOS service to exit the program
MAIN ENDP
END MAIN
