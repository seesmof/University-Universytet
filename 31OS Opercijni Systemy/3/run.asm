.model small 
.stack 100h 

.data
  msg db "JESUS CHRIST IS LORD",13,10,'$'

.code
main:
  mov ax,@data
  mov ds,ax 

  mov dx,offset msg 
  mov ah,9
  int 21h

  je stopret

stopfourch:
  mov ah,4ch
  int 21h

stopzeroh:
  mov ah,0h
  int 21h

stoptwentyh:
  int 20h

stopret:
  ret

end main
end