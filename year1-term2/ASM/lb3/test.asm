; This program demonstrates the use of different types of variables, output to console, and program procedures in assembly language.

; Data segment
data segment
    ; Define variables of different types and sizes
    byte_var db 10h ; 1-byte variable
    word_var dw 1234h ; 2-byte variable
    dword_var dd 56789012h ; 4-byte variable
    char_var db 'A' ; character variable
    string_var db 'Hello, world!', 0 ; null-terminated string
    array1 db 1, 2, 3, 4, 5 ; 1-dimensional array of bytes
    array2 dw 1, 2, 3, 4, 5 ; 1-dimensional array of words
    array3 dd 1, 2, 3, 4, 5 ; 1-dimensional array of dwords
    array4 db 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ; 2-dimensional array of bytes (2x5)
    array5 dw 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ; 2-dimensional array of words (2x5)
    array6 dd 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ; 2-dimensional array of dwords (2x5)
data ends

; Code segment
code segment
    assume cs:code, ds:data

    ; Define program procedures
    main proc
        ; Output byte variable to console
        mov ah, 2h ; 2h is the function code for outputting a character to console
        mov dl, byte_var
        int 21h

        ; Output word variable to console
        mov ah, 2h
        mov dx, word_var
        int 21h

        ; Output dword variable to console
        mov ah, 2h
        mov edx, dword_var
        int 21h

        ; Output character variable to console
        mov ah, 2h
        mov dl, char_var
        int 21h

        ; Output string variable to console
        mov ah, 9h ; 9h is the function code for outputting a string to console
        lea dx, string_var
        int 21h

        ; Output control characters to console
        mov ah, 2h
        mov dl, 0Dh ; CR
        int 21h
        mov dl, 0Ah ; LF
        int 21h
        mov dl, 8h ; BS
        int 21h

        ; Output array elements to console using LOOP statement
        mov cx, 5 ; set loop counter to 5
        mov si, offset array1 ; set source index to start of array1
        loop1:
            mov ah, 2h
            mov dl, [si] ; output byte at current index
            int 21h
            inc si ; increment source index
            loop loop1 ; repeat until loop counter is zero

        ; Output array elements to console using indexed addressing
        mov cx, 5 ; set loop counter to 5
        mov si, offset array2 ; set source index to start of array2
        mov di, 0 ; set destination index to zero
        loop2:
            mov ah, 2h
            mov dx, [si+di] ; output word at current index
            int 21h
            add di, 2 ; increment destination index by 2 (size of word)
            loop loop2 ; repeat until loop counter is zero

        ; Output array elements to console using base/index addressing
        mov cx, 5 ; set loop counter to 5
        mov esi, offset array3 ; set source index to start of array3
        mov edi, 0 ; set destination index to zero
        loop3:
            mov ah, 2h
            mov edx, [esi+edi*4] ; output dword at current index
            int 21h
            inc edi ; increment destination index by 1 (size of dword/4)
            loop loop3 ; repeat until loop counter is zero

        ; Output 2-dimensional array elements to console using nested LOOP statements
        mov cx, 2 ; set outer loop counter to 2 (number of rows)
        mov si, offset array4 ; set source index to start of array4
        loop4:
            mov cx, 5 ; set inner loop counter to 5 (number of columns)
            mov di, 0 ; set destination index to zero
            loop5:
                mov ah, 2h
                mov dl, [si+di] ; output byte at current index
                int 21h
                inc di ; increment destination index by 1 (size of byte)
                loop loop5 ; repeat until inner loop counter is zero
            add si, 5 ; increment source index by 5 (number of columns)
            mov ah, 2h
            mov dl, 0Dh ; CR
            int 21h
            mov dl, 0Ah ; LF
            int 21h
            loop loop4 ; repeat until outer loop counter is zero

        ; End program
        mov ah, 4ch ; 4ch is the function code for terminating the program
        int 21h
    main endp
code ends

end main ; end of program