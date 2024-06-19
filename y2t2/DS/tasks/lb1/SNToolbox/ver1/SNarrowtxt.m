function SNarrowtxt(x1, y1, x2, y2, txtstr, linecolour, textcolour);
if and(isstr(txtstr)==1, isstr(linecolour)==1)
   plot([x1 x2], [y1 y2], linecolour);
   c=(((x1-x2).^2)+((y1-y2).^2)).^(1./2);   
   c1=0.5.*c;
   alfa=asind(abs(y1-y2)./c); 
   if and(x2<=x1,y2>=y1)
      alfa=alfa+90;
   else
      if and(x2<=x1, y2<=y1)
         alfa=alfa+180;
      else
          if and(x2>=x1,y2<=y1)
             alfa=alfa+270;
          end;
      end;
   end;
   tx=c1.*cosd(alfa)+x1; ty=c1.*sind(alfa)+y1;
   ht=text(tx, ty, txtstr);
   set(ht,'Rotation',alfa);
   set(ht,'Color', textcolour);
end;
