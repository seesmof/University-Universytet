.MODEL SMALL
.STACK 100H

.DATA
    MSG1 DB 0DH, 0AH, "Enter the first number: $"
    MSG2 DB 0DH, 0AH, "Enter the second number: $"
    RESULT DB 0DH, 0AH, "Result in binary: $"
    BUFFER DB 9 DUP ('$') ; Buffer to store the binary representation

.CODE
.STARTUP
    MOV AX, @DATA
    MOV DS, AX

    ; Outputting a message to the console (message 1)
    MOV AH, 09H
    LEA DX, MSG1
    INT 21H

    ; Reading the first number from the console
    MOV AH, 01H
    INT 21H
    SUB AL, '0'
    MOV BL, AL

    ; Outputting a message to the console (message 2)
    MOV AH, 09H
    LEA DX, MSG2
    INT 21H

    ; Reading the second number from the console
    MOV AH, 01H
    INT 21H
    SUB AL, '0'
    MOV CL, AL

    ; Adding the numbers together
    ADD BL, CL

    ; Converting the result into binary
    MOV CH, 8
    LEA SI, BUFFER

CONVERT_LOOP:
    ROL BL, 1 ; Rotate left through carry
    ADC DL, 0 ; Add carry to DL
    ADD DL, '0' ; Convert DL to ASCII character
    MOV [SI], DL ; Store character in buffer
    INC SI

    LOOP CONVERT_LOOP

    ; Displaying the resulting text string to the console
    MOV AH, 09H
    LEA DX, RESULT
    INT 21H

    ; Displaying the binary representation from the buffer
    MOV DX, OFFSET BUFFER
    MOV AH, 09H
    INT 21H

.EXIT
    MOV AH, 4CH
    INT 21H
END
