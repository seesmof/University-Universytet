.model medium
.386
.stack
.data

    p1 db 'Enter operand 1:$'
    p2 db 'Enter operand 2:$'
    p3 db 'Enter operator (+ - * /):$'

.code
m   proc

    mov ax,@data
    mov ds,ax
    mov ax,0b800h
    mov es,ax
    mov di,7d0h
    mov ah,10100100b
    mov dh,ah

loopOne:

    mov ah,2
    mov bh,0
    mov dh,2
    mov dl,25
    int 10h

    mov ah,9
    mov dx,offset p1
    int 21h

    mov ah,1
    int 21h
    cmp al,30h

    jae failedFirst
    jmp loopOne

failedFirst:

    cmp al,39h
    jbe passedFirst
    jmp loopOne

passedFirst:
    sub al,30h
    push ax

loopTwo:

    mov ah,2
    mov bh,0
    mov dh,3
    mov dl,25
    int 10h

    mov ah,9
    mov dx,offset p2
    int 21h

    mov ah,1
    int 21h

    cmp al,30h
    jae failedSecond
    jmp loopTwo

failedSecond:
    cmp al,39h
    jbe passedSecond
    jmp loopTwo

passedSecond:
    sub al,30h
    push ax

operator:

    mov ah,2
    mov bh,0
    mov dh,4
    mov dl,25
    int 10h

    mov ah,9
    mov dx,offset p3
    int 21h
    mov ah,01h
    int 21h
    mov bl,al
    mov ah,02h
    mov bl,al
    mov ah,02h
    mov dl,0Ah
    int 21h

    cmp bl, '*'
    je multiplication

    cmp bl, '/'
    je division

    cmp bl, '+'
    je addition

    cmp bl, '-'
    je subtraction

    jmp operator

multiplication:
    pop bx
    pop ax

    mul bl

    mov bh,0
    mov bl,10
    div bl

    add al,30h
    add ah,30h
    mov bl,ah

    push ax
    mov ah,2
    mov dl,0Ah
    int 21h
    mov dl,0Dh
    int 21h
    pop ax

    mov ah,2
    mov bh,0
    mov dh,5
    mov dl,25
    int 10h

    mov ah,2
    mov dl,al
    int 21h

    mov ah,2
    mov dl,bl
    int 21h

    mov ah,2
    mov bh,0
    mov dh,6
    mov dl,25
    int 10h

    jmp getInp

addition:
    pop bx
    pop ax

    add al,bl
    mov ah,0
    AAA

    mov bx,ax
    add bh,48
    add bl,48

    push bx
    
    mov ah,2
    mov bh,0
    mov dh,5
    mov dl,25
    int 10h

    pop bx
    mov ah,2
    mov dl,bh
    int 21h

    mov ah,2
    mov dl,bl
    int 21h

    mov ah,2
    mov bh,0
    mov dh,6
    mov dl,25
    int 10h

    jmp getInp

subtraction:
    pop bx
    pop ax

    mov ch,0h

    cmp al,bl
    jb negative

solve:
    sub al,bl
    sub al,30h

    push ax

    mov ah,2
    mov dl,0Ah
    int 21h
    mov dl,0Dh
    int 21h

    mov ah,2
    mov bh,0
    mov dh,5
    mov dl,25
    int 10h

    cmp ch,1h
    je symbol

show:
    pop ax
    mov ah,2
    mov dl,al
    int 21h

    mov ah,2
    mov bh,0
    mov dh,6
    mov dl,25
    int 10h

    jmp getInp

negative:
    mov dl,al
    mov al,bl
    mov bl,dl
    mov ch,1h
    jmp solve

symbol:
    mov dl,'-'
    int 21h
    jmp show