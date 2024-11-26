function SNarrowtxt(x1, y1, x2, y2, txtstr, linecolour, textcolour);
if and(isstr(txtstr)==1, isstr(linecolour)==1)
    %annotation('arrow',[x1 x2], [y1 y2],'Color',linecolour);
    %c=(((x1-x2).^2)+((y1-y2).^2)).^(1./2);
    plot([x1 x2], [y1 y2], linecolour);
    if abs(x1-x2)<0.00001
        alfa=90;
    else
        alfa=atand((y1-y2)./(x1-x2));
    end;
    if y2>=y1
        alfa=alfa-180;
    end;
    a='v<^>';
    plot(x2,y2,a(fix((alfa+360)./90)));
    tx=(x1+x2)./2;
    ty=(y1+y2)./2;
    ht=text(tx, ty, txtstr,'Rotation',alfa,'HorizontalAlignment','center','Color', textcolour);
end;