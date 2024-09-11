.model small
.code
.stack 100h
start:
  mov ah,02h
  mov cl,41h
  mov dl,cl 
  int 21h
int 27h
end start