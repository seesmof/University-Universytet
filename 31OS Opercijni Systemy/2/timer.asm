.model small
.stack 100h

.data
  msg db "JESUS is LORD",13,10,'$'
  freq dw 165,156,165,0
  time dw 3 dup (100)

.code
start:
  mov ax,@data
  mov ds,ax

  lea si,freq
  lea bp,time

  mov di,[si]
  cmp di,0
  je stop

  mov bx,[bp]
  mov al,0b6h
  out 43h,al

  mov dx,14h 
  mov ax,4f38h 
  div di 
  out 42h,al 

  mov al,ah 
  out 42h,al 

  in al,61h
  mov ah,al 

  mov al,ah 
  out 61h,al 

  add si,2 
  add bp,2 

stop:
  mov ah,4ch
  int 21h
end start
