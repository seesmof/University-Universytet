hold on;
SNarrowtxt(0, 0, 2, 2, 'txtstr', 'r', [0 0.5 0.2]);
SNarrowtxt(0, 0, -2, 2, 'txtstr', 'g', [0.5 0 0.2]);
SNarrowtxt(0, 0, -2, -2, 'txtstr', 'b', [0.2 0 0.5]);
SNarrowtxt(0, 0, 2, -2, 'txtstr', 'k', [0 0 0]);
for i=1:1:30
   SNarrowtxt(10.*rand,12.*rand, 15.*rand, 8.*rand, 'EEEdsdd', 'r', [rand rand rand]);
end;
hold off;