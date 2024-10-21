.model small

.data
  vns db 'DOS Version $'
  ver db 12

.code
start:
  mov ax,@data
  mov ds,ax 

  mov dx,offset vns 
  mov ah,9 
  int 21h 

end start
