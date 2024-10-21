.model small
.stack 100h

.data
  msg db "JESUS is LORD",13,10,'$'
  truth db "JESUS CHRIST is the KING of kings and the LORD of lords",13,10,'$'

.code
start:
  mov ax,@data
  mov ds,ax

  mov dx,offset msg
  mov ah,9
  int 21h

  mov dx,offset truth 
  mov ah,9
  int 21h

  mov ah,4ch
  int 21h
end start
