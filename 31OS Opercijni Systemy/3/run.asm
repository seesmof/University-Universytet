.model small 
.stack 100h 

.data
  msg db "JESUS CHRIST IS LORD",13,10,'$'

.code
start:
  mov ax,@data
  mov ds,ax 

  mov dx,offset msg 
  mov ah,9
  int 21h

  je stop

stop:
  mov ah,4ch
  int 21h
end start