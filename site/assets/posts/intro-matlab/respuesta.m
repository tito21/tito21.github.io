% Respuesta al ejercio

% Datos
v = 10;
vx = v*cos(50*pi/180);
vy = v*sin(50*pi/180);
g = 9.8;
tf = 2*vy/g;

t = 0:0.01:tf; % un vector de tiempos discretizados

% posiciones en x e y
x = vx*t;
y = vy*t - 0.5*g*t.^2;

% graficamos en una nueva figura
figure;
plot(x,y)
grid();