.MODEL SMALL
.STACK 100H

.DATA
    MSG1 DB 0DH, 0AH, "Enter the first number: $"
    MSG2 DB 0DH, 0AH, "Enter the second number: $"
    RESULT1 DB 0DH, 0AH, "Result in decimal: $"
    RESULT2 DB 0DH, 0AH, "Result in binary: $"
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

    ; Displaying the result in decimal
    MOV AH, 0 ; Clear AH register
    MOV AL, BL ; Move the sum to AL register
    ADD AL, '0' ; Convert AL to ASCII
    MOV DX, OFFSET RESULT1
    MOV AH, 09H
    INT 21H

    ; Converting the result into binary
    MOV CH, 8
    MOV SI, OFFSET BUFFER
    MOV DL, AL ; Move the decimal result to DL
    ADD DL, '0' ; Convert DL to ASCII
    MOV AH, 02H ; Function to display a character
    INT 21H ; Display the decimal result character
CONVERT_LOOP:
    SHL BL, 1 ; Shift left through carry
    MOV AL, '0' ; Default value of '0' in AL

    ; Check carry flag to determine the current bit value
    JC SET_BIT
    MOV AL, '0' ; '0' if carry flag is clear
    ; Displaying the binary representation from the buffer
    MOV DX, OFFSET BUFFER
    MOV AH, 09H
    INT 21H

SET_BIT:
    MOV AL, '1' ; '1' if carry flag is set

STORE_BIT:
    MOV [SI], AL ; Store character in buffer
    INC SI

    LOOP CONVERT_LOOP

    ; Displaying the binary representation from the buffer
    MOV DX, OFFSET RESULT2
    MOV AH, 09H
    INT 21H

.EXIT
    MOV AH, 4CH
    INT 21H
END
