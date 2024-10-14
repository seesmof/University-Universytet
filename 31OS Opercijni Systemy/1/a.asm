.model small 
.stack 100h 
.data 

vns db 'DOS Version $'

.code 
main proc

mov ax,@data 
mov ds,ax 
mov dx,offset vns 
mov ah,9 
int 21h 

mov ah,30h 
int 21h 

main endp 
end 