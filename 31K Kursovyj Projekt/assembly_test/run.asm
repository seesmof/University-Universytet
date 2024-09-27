.model small
.stack 100h
.data
    iterations dw 0
    start_time dq 0
    end_time dq 0
    cpu_speed dq 0

.code
main proc
    ; Get the starting time
    rdtsc                ; Read the time-stamp counter
    shl edx, 32         ; Shift the high part to the left
    or eax, edx         ; Combine high and low parts
    mov start_time, eax  ; Store start time

    ; Perform a busy loop for a fixed duration
    mov cx, 1000000     ; Loop count
loop_start:
    inc iterations       ; Increment the iteration counter
    loop loop_start      ; Loop until cx is 0

    ; Get the ending time
    rdtsc                ; Read the time-stamp counter again
    shl edx, 32
    or eax, edx
    mov end_time, eax    ; Store end time

    ; Calculate CPU speed in MHz
    sub end_time, start_time  ; Calculate the elapsed cycles
    mov eax, iterations   ; Move the iteration count to eax
    mul dword ptr [1000000] ; Multiply by the number of cycles
    div end_time          ; Divide to get the speed in MHz
    mov cpu_speed, eax    ; Store the CPU speed

    ; Exit the program
    mov ax, 4C00h
    int 21h
main endp
end main